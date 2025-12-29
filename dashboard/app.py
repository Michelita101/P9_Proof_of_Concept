import streamlit as st

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
    st.info("Cette section présentera les tableaux et graphiques interactifs.")

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

