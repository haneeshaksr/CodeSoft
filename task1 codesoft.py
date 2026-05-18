print("====================================")
print("      WELCOME TO AI CHATBOT")
print("====================================")
print("Type 'bye' to exit the chatbot")

while True:
    user = input("You: ").lower()

    # Greeting messages
    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    # Asking chatbot condition
    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    # Asking chatbot name
    elif "your name" in user:
        print("Bot: My name is AI Rule-Based Chatbot.")

    # Asking about internship
    elif "internship" in user:
        print("Bot: CODSOFT provides Artificial Intelligence internships.")

    # Asking about Python
    elif "python" in user:
        print("Bot: Python is widely used for AI and Machine Learning.")

    # Thanking messages
    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    # Exit condition
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown messages
    else:
        print("Bot: Sorry, I don't understand that.")