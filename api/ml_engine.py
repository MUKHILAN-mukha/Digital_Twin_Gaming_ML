import joblib
from ml.features import extract_features
from analysis.rules import evaluate_rules

# LOAD MODEL AND ENCODER SEPARATELY
clf, encoder = joblib.load("ml/model.pkl")   # <-- FIXED

def analyze_with_ml(twin_data: dict):

    # Extract features for ML
    features = extract_features(twin_data)

    # ML prediction
    ml_pred_num = clf.predict([features])[0]
    ml_pred_label = encoder.inverse_transform([ml_pred_num])[0]

    # -----------------------------
    # FIX IS HERE ⬇️⬇️⬇️
    # Convert dict → object so rules.py can do twin.today_minutes
    twin_obj = type("Twin", (), twin_data)
    flags = evaluate_rules(twin_obj)
    # -----------------------------

    return {
        "ml_prediction": ml_pred_label,
        "rule_flags": flags
    }
