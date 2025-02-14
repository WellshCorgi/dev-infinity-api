import yfinance as yf
from fastapi import HTTPException

def get_stock_data(ticker: str):
    """주어진 종목(ticker)의 주가 데이터 조회"""
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")  # 1년치 데이터 가져오기
        if df.empty:
            raise ValueError(f"Unable to fetch data: {ticker}")
        return df
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Invalid ticker or no data available: {str(e)}")


def calculate_rsi(df, window=14):
    """RSI (Relative Strength Index) 계산"""
    delta = df["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    loss = loss.replace(0, 1e-10)  # 0으로 나누는 오류 방지
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_macd(df):
    """MACD (Moving Average Convergence Divergence) 계산"""
    short_ema = df['Close'].ewm(span=12, adjust=False).mean()
    long_ema = df['Close'].ewm(span=26, adjust=False).mean()
    macd = short_ema - long_ema
    macd_signal = macd.ewm(span=9, adjust=False).mean()
    return macd, macd_signal


def analyze_stock(ticker: str):
    """매수/매도 판단"""
    df = get_stock_data(ticker)

    # 이동 평균, RSI, MACD 계산
    df["50_MA"] = df["Close"].rolling(window=50).mean()
    df["200_MA"] = df["Close"].rolling(window=200).mean()
    df["RSI"] = calculate_rsi(df)
    df["MACD"], df["MACD_signal"] = calculate_macd(df)

    current_price = df["Close"].iloc[-1]
    ma50 = df["50_MA"].iloc[-1]
    ma200 = df["200_MA"].iloc[-1]
    rsi = df["RSI"].iloc[-1]
    macd = df["MACD"].iloc[-1]
    macd_signal = df["MACD_signal"].iloc[-1]

    # 거래량 (Volume) 추가 - 거래량이 증가하는 조건 추가
    volume_avg = df["Volume"].rolling(window=30).mean().iloc[-1]
    current_volume = df["Volume"].iloc[-1]

    # 신호 목록을 구조화된 데이터로 저장
    signals = []

    # 골든 크로스 / 데드 크로스
    if df["50_MA"].iloc[-2] < df["200_MA"].iloc[-2] and ma50 > ma200:
        signals.append({"type": "Buy", "reason": "Golden Cross (50-day MA > 200-day MA)"})
    if df["50_MA"].iloc[-2] > df["200_MA"].iloc[-2] and ma50 < ma200:
        signals.append({"type": "Sell", "reason": "Dead Cross (50-day MA < 200-day MA)"})

    # RSI 기반 과매수 / 과매도 판단
    if rsi < 30:
        signals.append({"type": "Buy", "reason": "RSI Oversold (<30)"})
    elif rsi > 70:
        signals.append({"type": "Sell", "reason": "RSI Overbought (>70)"})

    # 볼린저 밴드 활용
    bb_upper = df['Close'].rolling(window=20).mean() + (df['Close'].rolling(window=20).std() * 2)
    bb_lower = df['Close'].rolling(window=20).mean() - (df['Close'].rolling(window=20).std() * 2)

    if current_price < bb_lower.iloc[-1]:
        signals.append({"type": "Buy", "reason": "Price near lower Bollinger Band"})
    elif current_price > bb_upper.iloc[-1]:
        signals.append({"type": "Sell", "reason": "Price near upper Bollinger Band"})

    # MACD 상향 돌파 / 하향 돌파
    if df["MACD"].iloc[-2] < df["MACD_signal"].iloc[-2] and macd > macd_signal:
        signals.append({"type": "Buy", "reason": "MACD bullish crossover"})
    elif df["MACD"].iloc[-2] > df["MACD_signal"].iloc[-2] and macd < macd_signal:
        signals.append({"type": "Sell", "reason": "MACD bearish crossover"})

    # 추가적인 매매 신호 조건
    if current_price > ma50 and rsi < 40 and macd > macd_signal and current_volume > volume_avg:
        signals.append({"type": "Buy", "reason": "Multiple buy signals (MA, RSI, MACD, Volume)"})
    if current_price < ma50 and rsi > 60 and macd < macd_signal and current_volume > volume_avg:
        signals.append({"type": "Sell", "reason": "Multiple sell signals (MA, RSI, MACD, Volume)"})

    return {
        "symbol": ticker,
        "current_price": round(current_price, 2),
        "50_day_MA": round(ma50, 2),
        "200_day_MA": round(ma200, 2),
        "RSI": round(rsi, 2),
        "MACD": round(macd, 2),
        "MACD_signal": round(macd_signal, 2),
        "signals": signals if signals else [{"type": "Neutral", "reason": "No clear trading signal"}]
    }
