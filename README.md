# Sentiment Analysis API

This repository contains a simple Flask-based API for performing sentiment analysis on text. It uses a pre-trained model to classify the sentiment of a given text as either positive, negative, or neutral.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the API](#running-the-api)
- [API Endpoint](#api-endpoint)
    - [Request](#request)
    - [Response](#response)
- [Example Usage](#example-usage)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Description

This API provides a single endpoint (`/analyze`) that takes text as input and returns the sentiment classification (positive, negative, or neutral) as a JSON response. It's designed to be lightweight and easy to use, making it ideal for rapid prototyping and integration into other applications or frontends.

The sentiment analysis is performed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) model from the `nltk` library.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.6+:** You can download it from [python.org](https://www.python.org/downloads/).
- **pip:** The Python package installer, usually bundled with Python installations.

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    cd sentiment_analysis_tool
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the API

To start the Flask development server, run the following command:

```bash
python app.py
```

The API will be available at http://127.0.0.1:5000/.

### API Endpoint

```/analyze```

- **Method:** POST
- **Content-Type:** application/json
This endpoint is used to analyze the sentiment of a given text.

#### Request

The request body should be a JSON object with a single key text containing the text to be analyzed.

```bash
{
  "text": "The movie was fantastic!"
}
```

### Response

The API will respond with a JSON object that contains the analysis and the original text.

**Success Response (Status Code: 200):**

```json
{
  "input_text": "The movie was fantastic!",
  "sentiment": "Positive",
  "scores": {
    "neg": 0.0,
    "neu": 0.253,
    "pos": 0.747,
    "compound": 0.7351
  }
}

```
- **input_text:** The original text sent in the request.
- **sentiment:** The predicted sentiment, which will be either "Positive", "Negative", or "Neutral".
- **scores:** An object with the detailed scores from the VADER model, with keys neg, neu, pos, and compound.

### Error Responses

The API returns standard HTTP error codes with a JSON body that contains details about the error.

- **Status Code: 400 - Bad Request**

    ```json
    { "error": "No request body provided" }
    ```

    or

    ```json
    { "error": "Request body should contain a 'text' key" }
    ```

    or

    ```json
    { "error": "Invalid Content-Type. Please use application/json." }
    ```



- **Status Code: 415 - Unsupported Media Type**

- **Status Code: 500 - Internal Server Error**

    ```json
    { "error": "An internal server error occurred" }
    ```

## Example Usage

Here's how to send a request using `curl`:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "This product is terrible."}' \
  http://127.0.0.1:5000/analyze
```
The output of this command should be similar to the success response above.

## Error Handling

The API returns HTTP error status codes along with a JSON object explaining the error:

- **400:** Invalid or missing input data.
- **415:** Invalid content type.
- **500:** An unexpected server error occurred.

## Testing

The API includes a basic test suite that can be run as follows:

```bash
python -m unittest test_app.py
```
## Contributing

Feel free to contribute to this project by creating issues or submitting pull requests. For contributions, please follow these guidelines:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Add tests for your changes.
5. Submit a pull request.

## License

This project is licensed under the MIT License.