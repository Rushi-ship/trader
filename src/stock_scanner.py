import os
from dotenv import load_dotenv
from src.sentiment import get_sentiment_score
from src.indicators import calculate_indicators

load_dotenv()

async def get_recommendations():
    # Dummy data for now – later replace with actual API call
    stocks = ["INFY", "TCS", "RELIANCE"]
    recommendations = []

    for symbol in stocks:
        indicators = calculate_indicators(symbol)
        sentiment = get_sentiment_score(symbol)

        if indicators["rsi"] < 30 and sentiment > 0.5:
            recommendations.append({
                "symbol": symbol,
                "rsi": indicators["rsi"],
                "sentiment": sentiment,
                "reason": "Oversold + Positive sentiment"
            })

    return {"recommended": recommendations}
