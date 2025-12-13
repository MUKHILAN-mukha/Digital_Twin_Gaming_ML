from ml.features import extract_features
from analysis.rules import evaluate_rules
import joblib

clf, encoder = joblib.load("ml/model.pkl")

def analyze_with_ml(twin):
    features = extract_features(twin)
    ml_pred_num = clf.predict([features])[0]
    ml_label = encoder.inverse_transform([ml_pred_num])[0]

    rule_flags = evaluate_rules(twin)

    return {
        "ml_prediction": ml_label,
        "rule_flags": rule_flags
    }
