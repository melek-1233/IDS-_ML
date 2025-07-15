import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
from data_fetch import load_nsl_kdd

#chargement du dataset dans un data frame
df = load_nsl_kdd()

# simplification: 0=normal et 1=attaque
df["label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)

#encodage des colonness 
df = pd.get_dummies(df, columns=["protocol_type", "service", "flag"])

#séparation X / y
X = df.drop(columns=["label", "difficulty"])
y = df["label"]

#division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#notre modele supervisé RF
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

#faire l'evaluation
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

#sauvegarde du modele pour une futur utilisation
joblib.dump(clf, "rf_model.joblib")
print("✅ Modèle sauvegardé sous 'rf_model.joblib'")
