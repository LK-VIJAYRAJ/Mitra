def format_message(event, emotion):
    if emotion == "stress":
        return f"{event} — Breathe deep, you've got this. 💪"
    elif emotion == "joy":
        return f"{event} — Have fun and enjoy! 🎉"
    return f"{event} — Stay focused and balanced. 😊"
