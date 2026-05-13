import os
import requests
from openai import OpenAI

OPENAI_API_KEY = os.environ["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"]
TELEGRAM_BOT_TOKEN = os.environ["8403970315:AAHN-OVWvvsCsWghIIO4yos-txyIIMniEW8"]
TELEGRAM_CHAT_ID = os.environ["8066676686"]

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT = """
You are a Thai-language financial content writer.

Summarize today's important global financial news in Thai.
Focus on:
- Federal Reserve
- inflation
- stock market
- oil
- USD
- bonds
- geopolitics

Write concise investor-friendly summaries.
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": PROMPT}]
)

message = response.choices[0].message.content

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
    data={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    },
    timeout=30
)

print("Sent successfully")
