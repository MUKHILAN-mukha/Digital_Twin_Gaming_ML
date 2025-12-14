import joblib
from ml.features import extract_features

# load ONCE
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

model, encoder = joblib.load(MODEL_PATH)


def analyze_with_ml(twin: dict):
    features = extract_features(twin)

    # ML prediction
    pred_num = model.predict([features])[0]
    state = encoder.inverse_transform([pred_num])[0]

    alerts = []
    severity = "Low"

    if state == "Excessive":
        severity = "High"
        alerts.append("Daily usage exceeded threshold")

        if twin["aggregates"]["night_minutes"] > twin["thresholds"]["night"]:
            alerts.append("Late night gaming detected")

    elif state == "Moderate":
        severity = "Medium"
        alerts.append("Gaming time approaching limit")

    return {
        "state": state,
        "severity": severity,
        "alertmessage": alerts
    }
