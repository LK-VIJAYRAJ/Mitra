def basic_emotion_rule(text):
    text = text.lower()
    if any(word in text for word in ["review", "interview", "test", "diagnosis"]):
        return "stress"
    elif any(word in text for word in ["party", "celebration", "birthday", "date"]):
        return "joy"
    else:
        return "neutral"
