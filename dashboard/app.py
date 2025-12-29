import streamlit as st
import plotly.express as px
import pandas as pd

# Configuration de la page (WCAG 2.4.2 : titre de page)
st.set_page_config(
    page_title="P9 – Proof of Concept Dashboard",
    layout="wide"
)

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
        Les données correspondent à des tweets non vectorisés, utilisés en en entrée du pipeline de classification.
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
    st.info("Cette section permettra de tester le modèle de prédiction.")

# Page Accessibilité
elif page == "Accessibilité":
    st.title("Accessibilité du dashboard (WCAG)")
    st.write(
        """
        Cette application prend en compte les critères WCAG essentiels :
        - 1.1.1 Contenu non textuel
        - 1.4.1 Utilisation de la couleur
        - 1.4.3 Contraste minimum
        - 1.4.4 Redimensionnement du texte
        - 2.4.2 Titre de page
        """
    )

