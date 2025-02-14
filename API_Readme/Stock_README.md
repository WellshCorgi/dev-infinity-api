# Stock Analysis API

Dev Infinity API is a continuously evolving project focused on developing various features, designing efficient APIs, and documenting the entire process. Our goal is to create a scalable and well-structured API that meets modern development standards.

## 🚀 Features

- 📈 **Stock Market Analysis**: Fetch and analyze stock market data using `yfinance`.
- 🔄 **Technical Indicators**: Supports RSI, MACD, Moving Averages, Bollinger Bands, and more.
- 📡 **FastAPI Integration**: A high-performance API using FastAPI.
- ✅ **Automated Testing**: Comprehensive test coverage using `pytest`.
- 📝 **Well-Documented**: API documentation using Swagger UI (FastAPI provides interactive API docs by default).

## 🛠 Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.10+
- pip (Python package manager)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/dev-infinity-api.git
   cd dev-infinity-api
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
## 📡 Running the API Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Once the server is running, you can access the API documentation at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🧪 Running Tests

Run the test suite using `pytest`:

```bash
pytest tests/
```

## 📌 API Endpoints

### Stock Data

**GET** `/stock/{ticker}` → Fetch stock data and perform analysis.

Example Response:

```json
{
  "symbol": "AAPL",
  "current_price": 175.23,
  "50_day_MA": 170.45,
  "200_day_MA": 160.78,
  "RSI": 52.3,
  "MACD": 1.23,
  "MACD_signal": 1.10,
  "signals": ["Buy (Golden Cross)"]
}
```

## 📌 Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (feature/my-new-feature).
3. Commit your changes.
4. Push the branch and open a Pull Request.

## 📜 License

This project is licensed under the MIT License.

💡 Follow for updates and future enhancements!