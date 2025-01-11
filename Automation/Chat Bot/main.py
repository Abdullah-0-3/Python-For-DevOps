from chat_bot import get_ai_response
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            user_prompt = r.recognize_google(audio)
            print(f"You (spoken): {user_prompt}")
            return user_prompt
        except Exception as e:
            print("Could not understand audio. Please try again.")
            return ""

def get_user_input():
    print("Do you want to (1) Speak or (2) Type your question?")
    choice = input("Enter 1 for Speak or 2 for Type: ").strip()
    if choice == "1":
        return listen()
    elif choice == "2":
        user_prompt = input("You (typed): ")
        return user_prompt
    else:
        print("Invalid choice. Defaulting to typing.")
        user_prompt = input("You (typed): ")
        return user_prompt

def main():
    system_prompt = "Hello, how can I help you today? Be Short and precise. Stay Humble."
    system = "Hello, how can I help you today?"
    print(f"Bot: {system}")
    speak(system)

    while True:
        user_prompt = get_user_input()
        if user_prompt.lower() == "exit":
            print("Bot: Goodbye!")
            speak("Goodbye!")
            break
        response = get_ai_response(system_prompt, user_prompt)
        print(f"Bot: {response}")
        speak(response)
        system_prompt = response

if __name__ == "__main__":
    main()