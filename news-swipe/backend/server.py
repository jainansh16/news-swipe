# backend/server.py

from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# News API key (you should load this from an environment variable)
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

@app.route('/news', methods=['GET'])
def get_news():
    # Use query parameters to filter news (optional)
    category = request.args.get('category')
    country = request.args.get('country', 'us')  # Default to US news

    # Construct the News API URL
    news_api_url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
    if category:
        news_api_url += f'&category={category}'

    # Fetch news from the News API
    response = requests.get(news_api_url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch news'}), response.status_code

    # Return the JSON from News API directly or filter as needed
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
