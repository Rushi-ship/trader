from fastapi import FastAPI
from src.stock_scanner import get_recommendations

app = FastAPI()

@app.get("/recommendations")
async def recommend():
    return await get_recommendations()
