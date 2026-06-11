import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "your name": ["I am a chatbot.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["Sorry, I don't understand.", "Can you rephrase that?", "I'm not sure about that."]
}

def chatbot(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

# Main loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    
    if user.lower() == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break
    
    reply = chatbot(user)
    print("Chatbot:", reply)