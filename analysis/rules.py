def evaluate_rules(twin):
    flags = {
        "daily_limit": 0,
        "late_night": 0,
        "frequency": 0,
        "imbalance": 0
    }

    # RULE 1: Daily limit exceeded
    if twin.today_minutes > twin.daily_threshold:
        flags["daily_limit"] = 1

    # RULE 2: Night gaming threshold exceeded
    if twin.night_minutes > twin.night_threshold:
        flags["late_night"] = 1

    # RULE 3: Excessive sessions
    if twin.sessions_per_day > 15:
        flags["frequency"] = 1

    # RULE 4: Gaming imbalance (study vs gaming)
    if twin.gaming_ratio > 0.8:
        flags["imbalance"] = 1

    return flags
