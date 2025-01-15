import random

# Example heuristic-based logic
def get_response(message):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm functioning perfectly!",
        "bye": "Goodbye! Have a great day!",
    }
    message = message.lower()
    return responses.get(message, "Sorry, I didn't understand that.")
