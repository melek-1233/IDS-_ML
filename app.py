from flask import Flask, request, render_template
from data_fetch import load_nsl_kdd_test
import pandas as pd
import joblib

app = Flask(__name__)
clf = joblib.load("rf_model.joblib")

feature_columns = clf.feature_names_in_

#des valeurs par defaut réalistes d'une connexion potentiellement malveillante (a partir d'internet)
default_values = {
    'duration': 5,
    'src_bytes': 232,
    'dst_bytes': 815,
    'count': 10,
    'srv_count': 5,
    'serror_rate': 0.0,
    'same_srv_rate': 1.0,
    'diff_srv_rate': 0.0,
    'protocol_type_tcp': 1,
    'flag_SF': 1
}

#charge une ligne qui provoque une prediction dattaque
def get_attack_like_sample():
    df_test = load_nsl_kdd_test()
    df_test["label"] = df_test["label"].apply(lambda x: 0 if x == "normal" else 1)
    df_test = pd.get_dummies(df_test, columns=["protocol_type", "service", "flag"])

#Preparation des colonnes 
    X_all = df_test.drop(columns=["label", "difficulty"])
    X_model = pd.DataFrame(columns=clf.feature_names_in_)
    X_model = pd.concat([X_model, X_all], ignore_index=True).fillna(0)


#Conversion explicite des booleen/string en numerique
    X_model = X_model.replace({True: 1, False: 0, 'True': 1, 'False': 0})
    X_model = X_model.apply(pd.to_numeric, errors='coerce').fillna(0)


    for i in range(len(X_model)):
        sample = X_model.iloc[i:i+1]
        if clf.predict(sample)[0] == 1:
            return sample.iloc[0].to_dict()
    return default_values  # fallback si aucune attaque trouvé

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_data = default_values.copy()

    if request.method == "POST":
        action = request.form.get("action")

        if action == "normal":
            input_data = default_values.copy()
        elif action == "attaque":
            input_data = get_attack_like_sample()
        else:
            try:
                input_data = {}
                for col in feature_columns:
                    val = request.form.get(col, 0)
                    if val in ['True', 'true']:
                        input_data[col] = 1.0
                    elif val in ['False', 'false']:
                        input_data[col] = 0.0
                    else:
                        input_data[col] = float(val)

                sample = pd.DataFrame([input_data])
                prediction = clf.predict(sample)[0]
                result = "🚨 Intrusion detected" if prediction == 1 else "✅ Legitimate connection"
            except Exception as e:
                result = f"Erreur : {e}"

    return render_template("index.html", columns=feature_columns, values=input_data, result=result)

if __name__ == "__main__":
    app.run(debug=True)
