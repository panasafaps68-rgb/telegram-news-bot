import os

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
