# ml/features.py

def extract_features(twin_data):
    """
    Convert raw twin data into ML-friendly numeric features.
    """
    return [
        twin_data["today_minutes"],
        twin_data["night_minutes"],
        twin_data["sessions_per_day"],
        twin_data["gaming_ratio"]
    ]
