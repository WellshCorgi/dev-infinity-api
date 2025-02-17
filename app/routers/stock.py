from fastapi import APIRouter
from app.core.stock_analysis import analyze_stock

router = APIRouter(prefix="/stock", tags=["stock"])

@router.get("/{ticker}")
async def get_stock_analysis(ticker: str):
    """주식 분석 API"""
    result = analyze_stock(ticker)
    if "error" in result:
        return {"error": result["error"]}, 404
    return result