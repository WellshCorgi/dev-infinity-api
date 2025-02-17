from fastapi import FastAPI
from app.routers import stock, lotto

def create_app():
    app = FastAPI(title="dev-infinity API by WellshCorgi", version="1.0")
    app.include_router(stock.router)
    app.include_router(lotto.router)
    return app