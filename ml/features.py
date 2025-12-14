def extract_features(twin):
    agg = twin["aggregates"]

    today = agg["today_minutes"]
    weekly = agg["weekly_minutes"]
    night = agg["night_minutes"]
    sessions = agg["sessions_per_day"]

    return [today, weekly, night, sessions]