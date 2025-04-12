print("👋 Hello! I'm EmotiBot. Tell me how you're feeling today!")

# Main loop
while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        print("EmotiBot: It was nice talking to you! See you later 😊")
        break

    # Emotion detection
    if "happy" in user_input or "great" in user_input or "good" in user_input:
        print("EmotiBot: I'm so glad to hear you're feeling happy! 😊")
    elif "sad" in user_input or "down" in user_input or "depressed" in user_input:
        print("EmotiBot: I'm sorry you're feeling that way... I'm here for you. 💙")
    elif "angry" in user_input or "mad" in user_input or "annoyed" in user_input:
        print("EmotiBot: It's okay to be angry sometimes. Wanna talk about it? 😠")
    elif "tired" in user_input or "exhausted" in user_input or "sleepy" in user_input:
        print("EmotiBot: Sounds like you need some rest 😴. Take care of yourself!")
    else:
        print("EmotiBot: Hmm... I’m not sure what emotion that is, but I’m listening! 💬")
