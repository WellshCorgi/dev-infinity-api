# dev-infinity-api
A project focused on continuously developing various features, designing efficient APIs, and documenting the process along the way.


## 🚀 Features

- 🔄 **Continuous Development**: The project is consistently evolving, with new features, optimizations, and improvements being added regularly.
- 🤝 **Collaborative Code Enhancement**: Contributions from the community are encouraged to continuously refine and enhance the codebase.
- 📈 **Scalable and Efficient API**: Built with FastAPI to deliver high performance and scalability for various use cases.
- 🧪 **Automated Testing and Quality**: Includes thorough test coverage to ensure the stability and reliability of the API.
- 📝 **Comprehensive Documentation**: Well-documented with clear instructions, examples, and interactive API documentation (via Swagger UI and ReDoc).
- 🚀 **Feature-Rich**: Offers stock market analysis, technical indicators, and other advanced financial data analysis tools.


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