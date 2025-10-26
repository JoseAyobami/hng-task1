# String Analyzer Service

This is a FastAPI application that provides a REST API to analyze strings and store the analysis.

## Features

- **Analyze a string**: Calculates properties like length, palindrome status, unique characters, word count, SHA256 hash, and character frequency.
- **Store analysis**: Saves the analysis results in memory.
- **Retrieve analysis**: Fetches the analysis for a specific string.
- **List analyses**: Lists all stored analyses.
- **Filter analyses**: Filters the list of analyses by properties like palindrome status, length, word count, and contained characters.
- **Natural language filtering**: Provides an experimental endpoint to filter analyses using natural language queries.
- **Delete analysis**: Removes the analysis for a specific string.

## API Endpoints

- `POST /strings/`: Create a new string analysis.
- `GET /strings/{string_value}`: Retrieve the analysis for a specific string.
- `GET /strings/`: List all string analyses with optional filtering.
- `GET /strings/filter-by-natural-language`: Filter analyses using a natural language query.
- `DELETE /strings/{string_value}`: Delete the analysis for a specific string.
- `GET /`: Health check.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JoseAyobami/hng-task1
   cd hng-task1
   ```

2. Install the dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Application

Run the application using uvicorn:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

<!-- ## Usage

### Create a new string analysis

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/strings/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d 
  "{
  "value": "hello world"
}"
```

### Get a string analysis

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/strings/hello%20world' \
  -H 'accept: application/json'
```

### List all string analyses

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/strings/' \
  -H 'accept: application/json'
```

### Filter string analyses

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/strings/?is_palindrome=false&min_length=10' \
  -H 'accept: application/json'
```

### Filter with natural language

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/strings/filter-by-natural-language?query=palindromes%20longer%20than%205' \
  -H 'accept: application/json'
```

### Delete a string analysis

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/strings/hello%20world' \
  -H 'accept: application/json'
``` -->
