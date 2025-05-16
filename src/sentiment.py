import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_sentiment_score(symbol):
    # Replace with actual news + GPT call later
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": f"What's the market sentiment for {symbol}?"}
        ]
    )
    return 0.7  # Dummy score for now
