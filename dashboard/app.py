import streamlit as st
import plotly.express as px
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Configuration de la page (WCAG 2.4.2 : titre de page)
st.set_page_config(
    page_title="P9 – Proof of Concept Dashboard",
    layout="wide"
)

# Chargement du modèle DeBERTa-v3
@st.cache_resource
def load_model():
    model_name = "Michelita/deberta-p9-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    device = torch.device("cpu")
    model.to(device)
    model.eval()

    return tokenizer, model, device

tokenizer, model, device = load_model()

# Menu latéral
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Aller à",
    ["Accueil", "Données (EDA)", "Prédire", "Accessibilité"]
)

# Page Accueil
if page == "Accueil":
    st.title("Proof of Concept – Dashboard")
    st.subheader("Milestone 3 – Élaboration du dashboard")

    st.write(
        """
        Ce dashboard a pour objectif de :
        - présenter une analyse exploratoire des données,
        - démontrer le fonctionnement du moteur de prédiction,
        - respecter les critères d’accessibilité essentiels (WCAG).
        """
    )

    st.success("Application prête pour l’exploration 🚀")

# Page Données
elif page == "Données (EDA)":
    st.title("Analyse exploratoire des données")
    st.write(
        """
        Cette section présente un aperçu du jeu de données utilisé pour le projet.
        Les données correspondent à des tweets non vectorisés, utilisés en entrée du pipeline de classification.
        """
    )

    # Chargement des données
    @st.cache_data
    def load_data():
        return pd.read_parquet(
            "data/raw/tweets_16k.parquet"
        )

    df = load_data()
    
    label_mapping = {0: "Négatif", 4: "Positif"}
    df["sentiment"] = df["label"].map(label_mapping)

    #Informations générales
    st.subheader("Aperçu du jeu de données")
    st.write(f"Nombre de lignes : {df.shape[0]}")
    st.write(f"Nombre de colonnes : {df.shape[1]}")

    st.subheader("Répartition des classes")

    class_counts = df["label"].value_counts().sort_index()
    st.write(class_counts)

    st.dataframe(df.head(20))

    # Graphique simple : longueur des tweets
    st.subheader("Distribution de la longueur des tweets")

    df["tweet_length"] = df["text"].astype(str).str.len()

    fig = px.histogram(
        df,
        x="tweet_length",
        nbins=50,
        labels={"tweet_length": "Nombre de caractères"},
        title="Distribution de la longueur des tweets"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Ce graphique permet de visualiser la variabilité de la longueur des tweets, "
        "information utile pour le choix des modèles et des stratégies de prétraitement."
    )

# Page Prédiction
elif page == "Prédire":
    st.title("Démonstration du moteur de prédiction")

    st.write(
        """
        Cette section permet de tester le moteur de prédiction de sentiment
        basé sur le modèle DeBERTa entraîné dans le cadre du projet.
        """
    )

    user_input = st.text_area(
        "Saisissez un tweet en anglais :",
        placeholder="I really loved this product, it works perfectly!"
    )

    if st.button("Prédire"):
        if not user_input.strip():
            st.warning("Veuillez saisir un texte avant de lancer la prédiction.")
        else:
            # Tokenisation
            inputs = tokenizer(
                user_input,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=128
            )

            inputs = {k: v.to(device) for k, v in inputs.items()}

            # Prédiction
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                probs = torch.softmax(logits, dim=1)

                predicted_class = torch.argmax(probs, dim=1).item()
                confidence = probs[0][predicted_class].item()

            # Mapping des labels
            label_mapping = {0: "Négatif", 1: "Positif"}
            
            sentiment = label_mapping[predicted_class]
            confidence_pct = confidence * 100

            st.subheader("Résultat de la prédiction")
            st.write(f"**Sentiment prédit :** {sentiment}")
            st.write(f"**Score de confiance :** {confidence_pct:.1f} %")
            
            st.write(
                f"""
                - Probabilité Négatif : **{probs[0][0].item() * 100:.1f} %**
                - Probabilité Positif : **{probs[0][1].item() * 100:.1f} %**
                """
            )

# Page Accessibilité
elif page == "Accessibilité":
    st.title("Accessibilité du dashboard (WCAG)")

    st.write(
        """
        Cette application a été conçue en prenant en compte plusieurs critères
        essentiels d’accessibilité définis par les recommandations WCAG
        (Web Content Accessibility Guidelines).
        """
    )

    st.subheader("Critères d’accessibilité couverts")

    st.markdown(
        """
        **1.1.1 – Contenu non textuel**  
        Les graphiques sont systématiquement accompagnés de titres, de légendes
        et de commentaires textuels permettant d’en comprendre le contenu
        sans dépendre uniquement de la visualisation.

        **1.4.1 – Utilisation de la couleur**  
        L’information n’est jamais transmise uniquement par la couleur.
        Les résultats sont explicitement indiqués par du texte
        (ex. *Négatif* / *Positif*), indépendamment des codes visuels.

        **1.4.3 – Contraste minimum**  
        Les contrastes par défaut du thème Streamlit assurent une lisibilité
        suffisante entre le texte et l’arrière-plan, conformément aux seuils
        recommandés.

        **1.4.4 – Redimensionnement du texte**  
        Le contenu du dashboard reste lisible lorsque la taille du texte
        est augmentée via les paramètres du navigateur, sans perte
        d’information ni chevauchement.

        **2.4.2 – Titre de page**  
        Chaque page du dashboard dispose d’un titre clair et explicite,
        facilitant la navigation et la compréhension du contexte.
        """
    )

    st.success(
        "L’accessibilité a été intégrée dès la conception du dashboard, "
        "dans une logique de preuve de concept inclusive."
    )


