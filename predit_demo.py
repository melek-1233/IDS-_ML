import pandas as pd
import joblib
from data_fetch import load_nsl_kdd_test

#chargement du modele entraîné
clf = joblib.load("rf_model.joblib")

#chargement des donnees de test (depuis un repo open source sur GitHub)
df_test = load_nsl_kdd_test()

#pretraitement
df_test["label"] = df_test["label"].apply(lambda x: 0 if x == "normal" else 1)
df_test = pd.get_dummies(df_test, columns=["protocol_type", "service", "flag"])

# alignement des colonnes avec celles attendue par le modele
X_all = df_test.drop(columns=["label", "difficulty"])
X_model = pd.DataFrame(columns=clf.feature_names_in_)
X_model = pd.concat([X_model, X_all], ignore_index=True).fillna(0)

#prediction sur une ligne de test
sample = X_model.iloc[0:1]
prediction = clf.predict(sample)[0]
print("🔍 Prédiction sur une vraie connexion :", "✅ Normal" if prediction == 0 else "🚨 Attaque")
