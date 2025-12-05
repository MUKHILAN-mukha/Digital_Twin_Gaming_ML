def determine_severity(state):
    if state == "Healthy":
        return "NONE"
    elif state == "Moderate":
        return "LOW"
    else:
        return "HIGH"


def generate_alert(state, flags):
    if state == "Healthy":
        return ""

    messages = []

    if flags["daily_limit"]:
        messages.append("Daily gaming limit exceeded.")
    if flags["late_night"]:
        messages.append("Late-night gaming detected.")
    if flags["frequency"]:
        messages.append("Too many gaming sessions today.")
    if flags["imbalance"]:
        messages.append("High gaming-to-study ratio observed.")

    base = " ".join(messages)

    if state == "Moderate":
        return base + " Consider a soft warning."
    else:
        return base + " Strong alert recommended."
