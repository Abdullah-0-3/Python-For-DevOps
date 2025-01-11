from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

base_url = "https://api.aimlapi.com/v1"
api_key = os.getenv("AI_KEY")

api = OpenAI(api_key=api_key, base_url=base_url)

def get_ai_response(system_prompt, user_prompt):
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )
    return completion.choices[0].message.content