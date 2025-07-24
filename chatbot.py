import re
import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ['hi', 'hello', 'hey', 'namaste']
    greeting_responses = ['Hello!', 'Hi there!', 'Hey!', 'Namaste!']

    weather_keywords = ['weather', 'temperature', 'climate']
    weather_responses = [
        "The weather is great today!",
        "It's quite hot outside.",
        "Looks like it's going to rain.",
        "Cool and breezy!"
    ]

    name_keywords = ['your name', 'who are you', 'what is your name']
    name_responses = [
        "I am your friendly chatbot.",
        "You can call me Bot.",
        "I'm a simple AI assistant."
    ]

    thanks_keywords = ['thank you', 'thanks', 'thx']
    thanks_responses = [
        "You're welcome!",
        "No problem!",
        "Glad to help!"
    ]

    bye_keywords = ['bye', 'goodbye', 'see you']
    bye_responses = ['Goodbye!', 'See you later!', 'Bye! Have a nice day!']

    python_keywords = ['what is python', 'define python', 'python language']
    python_response = "Python is a powerful and easy-to-learn programming language used in web development, data science, AI, and more."

    if any(word in user_input for word in greetings):
        return random.choice(greeting_responses)

    elif any(word in user_input for word in weather_keywords):
        return random.choice(weather_responses)

    elif any(phrase in user_input for phrase in name_keywords):
        return random.choice(name_responses)

    elif any(word in user_input for word in thanks_keywords):
        return random.choice(thanks_responses)

    elif any(word in user_input for word in bye_keywords):
        return random.choice(bye_responses)

    elif any(phrase in user_input for phrase in python_keywords):
        return python_response

    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

def main():
    print("🤖 Bot: Hello! I am your simple chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Bot: Bye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("🤖 Bot:", response)

if __name__ == "__main__":
    main()
