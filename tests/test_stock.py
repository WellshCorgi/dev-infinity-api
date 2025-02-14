from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def fetch_stock_data(ticker: str):
    """Fetch stock data from the API for a given ticker"""
    return client.get(f"/stock/{ticker}")


def test_valid_stock():
    """Test for a valid stock ticker (AAPL)"""
    response = fetch_stock_data("AAPL")

    # Check if the response status code is 200
    assert response.status_code == 200, f"Response code: {response.status_code}"

    # Parse response data
    data = response.json()

    # Expected keys in the response
    expected_keys = [
        "symbol", "current_price", "50_day_MA", "200_day_MA",
        "RSI", "MACD", "MACD_signal", "signals"
    ]

    # Ensure all expected keys are present in the response
    for key in expected_keys:
        assert key in data, f"Response missing key: '{key}'"

    # Validate data types
    assert isinstance(data["symbol"], str), "symbol should be a string"
    assert isinstance(data["current_price"], (int, float)), "current_price should be a number"
    assert isinstance(data["signals"], list), "signals should be a list"


def test_invalid_stock():
    """Test for an invalid stock ticker"""
    response = fetch_stock_data("INVALID_TICKER")

    # Ensure the response status code is 404
    assert response.status_code == 404, f"Response code: {response.status_code}"

    # Validate error message
    verify_error_response(response, "Invalid ticker or no data available")


def test_empty_stock():
    """Test for a stock ticker with no available data"""
    response = fetch_stock_data("INVALID_SYMBOL")

    # Ensure the response status code is 404
    assert response.status_code == 404, f"Response code: {response.status_code}"

    # Validate error message
    verify_error_response(response, "Invalid ticker or no data available")


def verify_error_response(response, expected_message):
    """Verify that an error response contains the expected format and message"""
    data = response.json()

    assert "detail" in data, "Response missing 'detail' key"
    assert expected_message in data["detail"], f"Unexpected error message: {data['detail']}"
