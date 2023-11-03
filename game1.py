def chatbot():
    print("Hello! I'm a chatbot. Ask me anything.")

    while True:
        user_input = input("How can I assist you?: ").lower()

        if user_input == "what is your name":
            print(
                "My name is ChatGPT. I'm here to help you with information and tasks."
            )
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print(
                "I'm sorry, I don't understand that request. Ask me another question or type 'exit' to end the conversation."
            )


if __name__ == "__main__":
    chatbot()
