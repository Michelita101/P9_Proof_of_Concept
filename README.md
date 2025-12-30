# P9 – Proof of Concept  
## Dashboard de démonstration – Analyse de sentiments (NLP)

Ce projet s’inscrit dans le cadre du **Projet 9 – Développez une preuve de concept**
du parcours **Ingénieur en Intelligence Artificielle**.

L’objectif est de démontrer la faisabilité d’un moteur de **classification automatique
de sentiments** à partir de tweets en anglais, via un **dashboard interactif**.

---

## 🎯 Objectifs du projet

- Explorer et analyser un jeu de données de tweets non vectorisés (EDA)
- Démontrer le fonctionnement d’un modèle de classification de sentiments
- Rendre la démonstration accessible via une application web
- Intégrer des critères essentiels d’accessibilité (WCAG)
- Déployer le dashboard sur le cloud pour la démonstration

---

## 🎯 Périmètre du dashboard

Le dashboard couvre spécifiquement :

- l’analyse exploratoire du jeu de données (EDA)
- la démonstration d’un modèle de prédiction entraîné en amont
- l’affichage des résultats de prédiction et de leur score de confiance
- la prise en compte de critères essentiels d’accessibilité (WCAG)

Les étapes d’entraînement du modèle, d’expérimentation et de validation
ont été réalisées en amont (notebooks) et **ne font pas partie du périmètre du déploiement cloud**.

---

## 🧠 Données

- Jeu de données : tweets en anglais
- Labels d’origine :
  - `0` → sentiment négatif
  - `4` → sentiment positif
- Les données sont utilisées :
  - pour l’analyse exploratoire (EDA)
  - comme entrée du pipeline de classification

---

## 🤖 Modèle de prédiction

- Modèle utilisé : **DeBERTa fine-tuné**
- Type : classification binaire (Négatif / Positif)
- Framework : **PyTorch + Hugging Face Transformers**
- Le modèle produit :
  - une prédiction de classe
  - un score de confiance associé (probabilité)

⚠️ Remarque :  
Les labels du modèle sont internes (`0` / `1`) et distincts des labels d’origine du dataset (`0` / `4`).
Cette distinction est volontairement respectée dans le dashboard.

---

## 📊 Fonctionnalités du dashboard

Le dashboard Streamlit propose :

### 🏠 Accueil
- Présentation du contexte et des objectifs du POC

### 📈 Données (EDA)
- Aperçu du jeu de données
- Répartition des classes
- Visualisation de la longueur des tweets
- Commentaires explicatifs

### 🔮 Prédire
- Saisie libre d’un tweet en anglais
- Prédiction du sentiment
- Affichage du score de confiance
- Visualisation des probabilités par classe

### ♿ Accessibilité
- Présentation des critères WCAG pris en compte :
  - 1.1.1 Contenu non textuel
  - 1.4.1 Utilisation de la couleur
  - 1.4.3 Contraste minimum
  - 1.4.4 Redimensionnement du texte
  - 2.4.2 Titre de page

---

## ☁️ Déploiement

L’application est déployée sur **Streamlit Community Cloud** afin de permettre
une démonstration accessible sans configuration locale.

Le déploiement cloud s’inscrit dans une logique de **preuve de concept**,
sans objectif de mise en production industrielle.

---

## 🚀 Lancer l’application en local (optionnel)

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## 📝 Auteur

Projet réalisé par **Michèle Dewerpe**  
Dans le cadre du parcours *Ingénieur IA – OpenClassrooms*
