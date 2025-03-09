# Money Making Machine - Streamlit App

This is a Streamlit-based web application that provides a fun and interactive way to generate random money amounts, discover side hustle ideas, and get motivational money quotes.

## Features
- **Instant Cash Generator**: Click a button to generate a random amount of money.
- **Side Hustle Ideas**: Get a random side hustle suggestion from an API.
- **Money Motivational Quotes**: Receive a random money-related motivational quote.

## Installation & Usage
### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies
```bash
pip install streamlit requests
```

### 3. Run the Streamlit App
```bash
streamlit run main.py
```

### 4. API Requirements
This app interacts with a FastAPI server running locally. Ensure the FastAPI server is up and running at `http://127.0.0.1:8000` before using the side hustle and money quote features.

## API Endpoints Used
- `GET /side_hustles?apiKey=12345`: Returns a random side hustle idea.
- `GET /money_quotes?apiKey=12345`: Returns a random money-related quote.

## Dependencies
- **Streamlit** (for web interface)
- **Requests** (for API calls)
- **Random & Time** (built-in Python modules)

## Common Issues & Fixes
- **Typo in `st.success()`**: Ensure `st.sucess()` is corrected to `st.success()`.
- **API Connection Errors**: Ensure the FastAPI server is running and accessible at `http://127.0.0.1:8000`.

## Author
Bisma Yousuf

## License
This project is licensed under the MIT License.
