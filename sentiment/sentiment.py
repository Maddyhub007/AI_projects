import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()   # 👈 THIS IS IMPORTANT

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_sentiment(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Reply only with Positive, Neutral, or Negative"},
            {"role": "user", "content": text}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()