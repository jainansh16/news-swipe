# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# import requests
# import pandas as pd
# import logging

# app = Flask(__name__)
# CORS(app)

# liked_articles = []  # This will store article descriptions temporarily

# @app.route('/news', methods=['GET'])

# def main():
    
#     url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=a4f7fdd20a1942b8bb0dd41326f21a72')
    
#     response = requests.get(url)
#     if response.status_code == 200:

#         articles = response.json().get('articles', [])
#         filtered_articles = filter_articles(articles)
#         filtered_articles = filtered_articles[:6]

#         return jsonify({'articles': filtered_articles, 'status': 'ok', 'totalResults': len(filtered_articles)})
    
#     else:
    
#         return jsonify({'error': 'Failed to fetch news'}), response.status_code

# def filter_articles(articles):
#     processed_articles = []
#     for article in articles:
#         if article.get('urlToImage', ''):
#             processed_articles.append(article)

#     return processed_articles

# @app.route('/like', methods=['POST'])
# def like_article():
#     description = request.json.get('description')
#     liked_articles.append(description)
#     return jsonify({'status': 'Article description saved'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from collections import Counter
import re
import nltk
from textblob import TextBlob


app = Flask(__name__)
CORS(app)

liked_articles = []  # This will store article descriptions temporarily

@app.route('/news', methods=['GET'])
def fetch_news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=a4f7fdd20a1942b8bb0dd41326f21a72'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        filtered_articles = [article for article in articles if article.get('urlToImage')]
        return jsonify({'articles': filtered_articles[:6], 'status': 'ok', 'totalResults': len(filtered_articles)})
    else:
        return jsonify({'error': 'Failed to fetch news'}), response.status_code

@app.route('/like', methods=['POST'])
def like_article():
    description = request.json.get('description')
    if description:
        liked_articles.append(description)
        return jsonify({'status': 'Description saved'}), 200
    else:
        return jsonify({'error': 'No description provided'}), 400

@app.route('/recommend', methods=['GET'])
def recommend_articles():
    # For demonstration, this could return the most recently liked article descriptions
    if liked_articles:
        return jsonify({'recommended_articles': liked_articles}), 200
    else:
        return jsonify({'error': 'No articles to recommend'}), 404

@app.route('/keywords', methods=['GET'])
def analyze_keywords():
    if not liked_articles:
        return jsonify({'error': 'No keywords to analyze'}), 404

    all_keywords = []
    for description in liked_articles:
        keywords = extract_keywords(description)
        all_keywords.extend(keywords)

    keyword_counts = Counter(all_keywords)
    most_common_keywords = keyword_counts.most_common(10)
    print("Most Common Keywords: ", most_common_keywords)

    return jsonify({'most_common_keywords': most_common_keywords}), 200

def extract_keywords(text):
    blob = TextBlob(text)
    return [phrase for phrase in blob.noun_phrases]
    # """Extract keywords by removing special characters, splitting text, and removing common words."""
    # common_words = {'the', 'in', 'on', 'at', 'and', 'to', 'for', 'with', 'a', 'an', 'of', 'was', 'by', 'it', 'if', 'all', 'you'}
    
    # # Remove special characters and digits
    # cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # # Convert to lowercase to standardize for comparison
    # words = set(cleaned_text.lower().split())
    
    # # Remove common words
    # keywords = words - common_words
    # return list(keywords)

if __name__ == '__main__':
    app.run(debug=True)