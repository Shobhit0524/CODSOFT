def chatbot():
    print(" ChatBot: Hi! I'm RuleBot. Ask me anything (type 'exit' to quit).")
    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print(" ChatBot: Hello! How can I help you today?")
        elif "your name" in user_input:
            print(" ChatBot: I'm RuleBot, your friendly chatbot!")
        elif "how are you" in user_input:
            print(" ChatBot: I'm just code, but I'm doing great!")
        elif "bye" in user_input or "exit" in user_input:
            print(" ChatBot: Goodbye! Have a great day!")
            break
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f" ChatBot: The current time is {now.strftime('%H:%M:%S')}")
        else:
            print(" ChatBot: Sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
