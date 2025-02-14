from fastapi import FastAPI


def create_app():
    app = FastAPI(title="dev-infinity API by WellshCorgi", version="1.0")
    from app.routers import stock
    app.include_router(stock.router)
    return app