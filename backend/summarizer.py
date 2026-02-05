import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📝 Generate article from topic
def generate_article(topic: str) -> str:
    prompt = f"""
Write a detailed, well-structured article about the following topic:

Topic: {topic}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


# ✂️ Summarize article
def summarize_text(paragraph: str, word_limit: int) -> str:
    prompt = f"""
Summarize the following text into approximately {word_limit} words.

Text:
{paragraph}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
