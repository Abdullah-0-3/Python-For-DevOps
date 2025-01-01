import requests
import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speak(text):
    """Helper function for speaking text."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_top_news(category="general", country="us", count=3):
    """
    Fetches top news headlines along with URLs and descriptions.

    Args:
    - category: News category (e.g., general, business, sports).
    - country: Country code (e.g., us, in, gb).
    - count: Number of headlines to return.

    Returns:
    - A list of dictionaries containing title, description, and URL of news articles.
    """
    try:
        params = {
            "apiKey": NEWS_API_KEY,
            "category": category,
            "country": country,
            "pageSize": count,
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        news_data = response.json()

        if news_data["status"] == "ok":
            articles = [
                {
                    "title": article["title"],
                    "description": article["description"] or "Description not available.",
                    "url": article["url"]
                }
                for article in news_data["articles"]
            ]
            return articles
        else:
            return []
    except Exception as e:
        return f"An error occurred: {str(e)}"

def handle_news_request(command):
    """Handles user request for news headlines."""
    # Determine category from the command
    if "business" in command:
        category = "business"
    elif "sports" in command:
        category = "sports"
    elif "technology" in command:
        category = "technology"
    else:
        category = "general"

    speak(f"Fetching the latest {category} news...")
    news = get_top_news(category=category, country="us", count=3)

    if not news:
        speak("Sorry, I couldn't fetch the news right now.")
        return

    # Announce and display headlines
    for i, article in enumerate(news):
        speak(f"Headline {i+1}: {article['title']}")
        print(f"{i+1}. {article['title']}")

    # Ask user for details
    speak("Would you like details about any of these? Say 'first', 'second', or 'third'.")
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
            choice = recognizer.recognize_google(audio).lower()
            if "first" in choice:
                selected_article = news[0]
            elif "second" in choice:
                selected_article = news[1]
            elif "third" in choice:
                selected_article = news[2]
            else:
                speak("I didn't understand your choice.")
                return

            # Read the selected article
            speak(f"Here's the full story: {selected_article['description']}")
            speak(f"For more details, visit: {selected_article['url']}")
            print(f"Description: {selected_article['description']}")
            print(f"URL: {selected_article['url']}")
        except Exception as e:
            print(f"Error: {str(e)}")
            speak("Sorry, I couldn't process your request.")