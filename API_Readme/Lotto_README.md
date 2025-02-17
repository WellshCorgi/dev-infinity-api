# Stock Analysis API

Dev Infinity API is a continuously evolving project focused on developing various features, designing efficient APIs, and documenting the entire process. Our goal is to create a scalable and well-structured API that meets modern development standards.

## 🚀 Features

- 🎰 **Lotto Number Lookup**: Check past lottery results and winning numbers.
- 🎲 **Lotto Number Generator**: Generate random lottery numbers for your next draw.
- ⏳ **Excitement Until Draw Day**: Track upcoming draw dates and build anticipation.
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


## 📌 API Endpoints

### Genereating Lotto number 

**GET** `/lotto/gen?sets=1` → Make lotto numbers about sets times and latest winning data.

Example Response:

```json
{
  "message": "Lotto numbers generated successfully",
  "timestamp": "2025-02-17T13:06:34.732115",
  "generated_numbers": [
    {
      "numbers": [
        2,
        5,
        12,
        15,
        18,
        38
      ],
      "bonus": 26
    }
  ],
  "latest_draw": {
    "draw_no": 1159,
    "draw_date": "2025-02-15",
    "numbers": [
      3,
      9,
      27,
      28,
      38,
      39
    ],
    "bonus": 7
  }
}
```

### Search Lotto winning number
**GET** `/lotto/search?round_num=1024` → Search lotto winning number about (round_num).

```json
{
  "draw_no": 1024,
  "draw_date": "2022-07-16",
  "numbers": [
    9,
    18,
    20,
    22,
    38,
    44
  ],
  "bonus": 10
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