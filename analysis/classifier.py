def classify_behavior(flags):
    total = sum(flags.values())

    if total == 0:
        return "Healthy"
    elif total == 1:
        return "Moderate"
    else:
        return "Excessive"
