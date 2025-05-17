# 📈 Stock Recommendation API

This is a GenAI-powered stock recommendation engine that filters NSE stocks based on:
- 📊 Technical indicators (like RSI)
- 🧠 News sentiment score
- 💰 Price action logic

---

## 🔗 Live Swagger Docs
> http://localhost:8000/docs

---

## ⚙️ Endpoints

### 🚀 GET `/recommendations`

Returns a list of recommended stocks with buy/avoid suggestions.

#### ✅ Headers:
```http
Authorization: Bearer <your_token_here>

**Sample Response**
[
  {
    "symbol": "INFY",
    "score": 82,
    "sentiment": "Bullish",
    "reason": "Oversold + Positive sentiment",
    "action": "BUY",
    "target": 1570.25,
    "stop_loss": 1440.55,
    "current_price": 1495.00
  },
  {
    "symbol": "TCS",
    "score": 74,
    "sentiment": "Neutral",
    "reason": "No strong entry signal",
    "action": "AVOID",
    "target": null,
    "stop_loss": null,
    "current_price": 3400.00
  }
]

🔬 Postman Collection

Use the included collection to test this API in Postman.
File: Stock-API-Collection.json
Auth token placeholder is already set
Just hit Send on /recommendations

🧑‍💻 Built With

FastAPI 🚀
Pydantic 🧱
Async Python 🐍
Swagger UI 🧪
stock.indianapi.in (coming soon)


---

### Save the file

Then run this in terminal (if you're on Git):
```bash
git add README.md
git commit -m "Updated README with docs"
git push

--------
Rushi Eswar 🇮🇳
Fintech Product Manager | AI Generalist
Contact - https://linkedin.com/in/rushi-eswar

