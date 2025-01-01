import speech_recognition as sr
import pyttsx3
import webbrowser

from modules import music_library
from modules.weather import get_weather
from modules.chat_gemini import get_ai_response
from modules.news import handle_news_request

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Speak Function
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Listen Function
def listen():
    recognizer = sr.Recognizer()
    print("Initializing Jarvis...")
    print("Listening...")

    while True:
        try:
            with sr.Microphone() as source:
                # Initial listening for wake word
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
            command = recognizer.recognize_google(audio).lower()

            if "jarvis" in command:  # Wake word detected
                speak("Jarvis Activating...")
                print("Jarvis Active...")
                speak("Yaaa! How can I help you?")
                
                while True:  # Enter conversation loop
                    try:
                        with sr.Microphone() as source:
                            print("Listening for your command...")
                            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
                        command = recognizer.recognize_google(audio).lower()

                        print(f"You said: {command}")
                        print("Processing command...")

                        if "exit" in command:
                            speak("Jarvis is shutting down...")
                            return  # Exit the entire program

                        process_command(command)  # Process the recognized command

                    # except sr.UnknownValueError:
                    #     speak("Sorry, I didn't catch that. Could you repeat?")
                    # except sr.RequestError:
                    #     speak("Sorry, there's a problem with the speech recognition service.")
                    except Exception as e:
                        print(f"Error: {str(e)}")
                        # speak("An unexpected error occurred.")
        except sr.UnknownValueError:
            print("Waiting for 'Jarvis' wake word...")
        except sr.RequestError:
            print("Speech recognition service error.")
        except Exception as e:
            print(f"Error: {str(e)}")

# Process Command Function
def process_command(command):
    if "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn...")
        webbrowser.open("https://www.linkedin.com")
    elif "play" in command:
        song = command.split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "weather" in command or "temperature" in command:
        handle_weather_request(command)
    elif "news" in command:
        handle_news_request(command)  # Handle news requests
    else:
        # AI Response for Unrecognized Commands
        system_prompt = (
            "Jarvis is a virtual assistant that helps you with daily tasks. "
            "How can I help you today? Be concise unless more details are requested."
        )
        response = get_ai_response(system_prompt, command)
        speak(response)
        print(f"Jarvis: {response}")
    return False

# Handle Weather Requests
def handle_weather_request(command):
    speak("Fetching weather information...")
    response = get_weather('Islamabad')
    print(response.text)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    listen()