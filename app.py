from flask import Flask, request, jsonify, logging
from model import analyze_sentiment
from flask_cors import CORS  
import json
import logging

app = Flask(__name__)
CORS(app)  
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if request.content_type != 'application/json':
            logger.error(f"Invalid Content-Type: {request.content_type}")
            return jsonify({'error': 'Invalid Content-Type. Please use application/json.'}), 415
        data = request.get_json()
        if not data:
          logger.error("No request body provided")
          return jsonify({'error': 'No request body provided'}), 400
        if 'text' not in data:
            logger.error("Request body should contain a 'text' key")
            return jsonify({'error': 'Request body should contain a "text" key'}), 400
        text = data['text']

        if not text or not text.strip():
            logger.warning("Empty or whitespace text provided")
            return jsonify({'sentiment': 'Neutral', 'message': 'Empty or whitespace text provided'}) , 200

        analysis = analyze_sentiment(text)
        return jsonify({'input_text':text,'sentiment': analysis['sentiment'], "scores": analysis['scores']}), 200
    except Exception as e:
        logger.exception("An error occurred during sentiment analysis:")
        return jsonify({'error': 'An internal server error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)