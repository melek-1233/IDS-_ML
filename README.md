# 🔐 Network Intrusion Detection System (IDS) with Machine Learning

Ce projet implémente un **système de détection d'intrusion (IDS)** basé sur l'apprentissage automatique, capable d'identifier les connexions réseau malveillantes grâce au jeu de données **NSL-KDD**.

L'application propose :
- Entraînement d’un modèle de classification supervisé (Random Forest),
- Évaluation du modèle,
- Prédiction sur de vraies connexions issues du dataset de test,
- Interface web intuitive avec Flask pour simuler des connexions réseau.

---

## 📁 Structure de base du projet
```jsx
data_fetch.py # Téléchargement et chargement des datasets NSL-KDD (train & test)
model_train.py # Préparation, entraînement, évaluation et sauvegarde du modèle Random Forest
predict_demo.py # Démonstration de prédiction sur une ligne du dataset de test
app.py # Application Flask pour prédire visuellement une connexion réseau
templates / index.html # Interface HTML Bootstrap pour l'application Flask
rf_model.joblib # Modèle sauvegardé (généré après exécution de model_train.py)
```


---

## 📦 Jeu de données

Utilisation du jeu de données **NSL-KDD**, disponible sur [GitHub – Jehuty4949](https://github.com/Jehuty4949/NSL_KDD).

- `KDDTrain+.csv` : dataset d’entraînement
- `KDDTest+.csv` : dataset de test

Aperçu visuel des premières lignes des deux jeux de données train et test :
![Image](https://github.com/user-attachments/assets/65e6adc3-0398-47f1-800f-ec198054422f)

---

## ⚙️ Entraînement du modèle

L’entraînement est réalisé avec un **Random Forest Classifier** après un prétraitement :
- Encodage one-hot,
- Mapping des labels (normale vs attaque),
- Séparation en features (X) et étiquettes (y).

**Exécution :**

```bash
python model_train.py
```
![Image](https://github.com/user-attachments/assets/1355e342-58eb-45c0-820a-4d3171c73feb)

---

## 🤖 Test de prédiction 

Ce script permet de prédire le type (normal ou attaque) d'une ligne prise au hasard dans le jeu de test.

```bash
python predict_demo.py
```

![Image](https://github.com/user-attachments/assets/2d423002-63d0-4613-b479-4bca898b6044)

---

## 🌐 Interface Web avec Flask

L'application web app.py permet de:

- Remplir un formulaire simulant une connexion réseau,

- Pré-remplir les champs avec une connexion normale ou une attaque simulée,

- Afficher le résultat de la prédiction avec des visuels et icônes claires.

Lancer l'application : 

```bash
python app.py
```
Aperçu de l'interface :

<img width="1856" height="1680" alt="Image" src="https://github.com/user-attachments/assets/3c9e49a4-a8f3-483f-9aef-8b11132e7ba2" />

Exemple avec une connexion saine :

<img width="671" height="4096" alt="Image" src="https://github.com/user-attachments/assets/8eb20017-d086-4048-8f25-81035097d599" />


Exemple avec une connexion malveillante détectée :

<img width="671" height="4096" alt="Image" src="https://github.com/user-attachments/assets/07cef466-ac42-480e-aedd-690588124ed2" />






