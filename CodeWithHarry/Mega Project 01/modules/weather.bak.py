from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("CHAT_API_KEY")
base_url = "https://api.aimlapi.com/v1"

# Initialize OpenAI API
api = OpenAI(api_key=api_key, base_url=base_url)

# Define a reusable system prompt for weather
SYSTEM_PROMPT = (
    "Provide a concise current weather update for the location requested. "
    "If no location is specified, assume Islamabad as default."
)

# Get Weather Response Function
def get_weather_response(user_prompt):
    try:
        completion = api.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=256,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error fetching weather response: {str(e)}"
