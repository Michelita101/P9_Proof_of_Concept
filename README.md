# P9 – Proof of Concept  
## Analyse de sentiments sur tweets – Comparaison BERT vs DeBERTa-v3

Ce projet s’inscrit dans le cadre du **Projet 9 – Développez une preuve de concept** du parcours **Ingénieur en Intelligence Artificielle (OpenClassrooms)**.

L’objectif est de **tester et comparer une architecture Transformer récente (DeBERTa-v3)** à une **baseline éprouvée (BERT)** sur une tâche de **classification de sentiments sur tweets**, et de rendre les résultats accessibles via un **dashboard interactif déployé sur le cloud**.

---
## 🔗 Ressources du projet

- 📊 Dashboard Streamlit : https://p9proofofconcept-michelita.streamlit.app/
- 💻 Code source complet : https://github.com/Michelita101/P9_Proof_of_Concept

## 🎯 Objectifs du projet

- Réaliser une **veille scientifique** sur les architectures Transformer récentes
- Implémenter une **preuve de concept** basée sur DeBERTa-v3
- Comparer les performances avec une **baseline BERT**
- Analyser les résultats à l’aide de métriques adaptées (Accuracy, F1-score)
- Interpréter le modèle via des approches d’**interprétabilité globale et locale (SHAP)**
- Déployer un **dashboard interactif accessible** pour démontrer le fonctionnement du modèle

---

## 🧠 Données

- Dataset : extrait du **Twitter Sentiment Analysis dataset**
- Volume : ~16 000 tweets en anglais
- Labels :
  - `0` → sentiment négatif
  - `4` → sentiment positif
- Dataset équilibré (50 / 50)

Caractéristiques principales :
- textes courts (~65–70 caractères en moyenne)
- langage bruité, informel, parfois ambigü

---

## 🤖 Modélisation

### 🔹 Baseline
- Modèle : **BERT**
- Objectif : référence robuste issue d’un projet précédent

### 🔹 Modèle testé
- Modèle : **DeBERTa-v3 (fine-tuné)**
- Framework : **PyTorch + Hugging Face Transformers**

### 🔹 Hypothèse
Évaluer si une architecture récente basée sur une **attention désentrelacée** permet d’améliorer la performance sur des textes courts et ambigüs.

---

## 📊 Résultats

| Modèle       | Accuracy | F1-score | Temps d’entraînement |
|--------------|----------|----------|----------------------|
| BERT         | 0.833    | 0.834    | ~1 min               |
| DeBERTa-v3   | 0.843    | 0.842    | ~3 min               |

### 🔍 Lecture

- Gain mesurable sur toutes les métriques
- Amélioration particulièrement pertinente sur le **F1-score**
- Réduction des **faux négatifs**
- Coût computationnel plus élevé

Conclusion :  
**DeBERTa-v3 apporte un gain réel mais modéré, à arbitrer selon le contexte d’usage**

---

## 🔎 Interprétabilité

Le modèle a été analysé via **SHAP** :

- **Interprétabilité globale** :
  - identification des tokens les plus influents
  - prise en compte des signaux émotionnels et structurels

- **Interprétabilité locale** :
  - analyse de prédictions individuelles
  - compréhension du rôle des mots de contraste (*but*, *not*)

Le modèle ne se contente pas de compter les mots, il interprète la **structure de la phrase**.

---

## 📊 Dashboard interactif

Un dashboard a été développé avec **Streamlit** pour rendre le modèle accessible.

### Fonctionnalités :

- 📈 **EDA** :
  - distribution des classes
  - longueur des tweets

- 🔮 **Prédiction** :
  - saisie libre de texte
  - classification (positif / négatif)
  - score de confiance

- ♿ **Accessibilité (WCAG)** :
  - contraste
  - lisibilité
  - information non dépendante de la couleur
  - structure claire

---

## ☁️ Déploiement

Le dashboard est accessible en ligne :

👉 [Accéder à l'application Streamlit](https://p9proofofconcept-michelita.streamlit.app/)

Déploiement réalisé via **Streamlit Community Cloud**  
dans une logique de **proof of concept (non industrielle)**.

---

## 📁 Structure du projet
```
P9_Proof_of_Concept/
│
├── notebook/                 # Modélisation et comparaison des modèles
├── note_methodologique/      # Note de cadrage et démarche
├── plan prévisionnel/        # Plan de travail initial
├── dashboard/                # Application Streamlit
├── README.md
```

---

## 🚀 Lancer l’application en local

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## ⚠️ Limites du projet

- Dataset simplifié (tweets sans emojis)
- Optimisation des hyperparamètres non exhaustive (seuil de décision par exemple)
- Interprétabilité partielle (modèle Transformer complexe)

---

## 🔮 Perspectives

- Optimisation fine des hyperparamètres
- Exploration de modèles plus légers ou multimodaux
- Intégration d’éléments contextuels (emoji, sarcasme)

---

## 📝 Auteur

Projet réalisé par **Michèle Dewerpe**  
Dans le cadre du parcours *Ingénieur en Intelligence Artificielle – OpenClassrooms*
