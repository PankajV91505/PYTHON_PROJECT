import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
        "how are you": ["I'm just a bot, but I'm doing great!", "I'm good, how about you?"],
        "bye": ["Goodbye!", "See you later!", "Take care!"]
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

def main():
    print("Simple Chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
