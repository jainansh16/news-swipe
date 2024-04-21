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
all_keywords = {}

current_page = 1
@app.route('/news', methods=['GET'])
def fetch_news():
    global current_page
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=a4f7fdd20a1942b8bb0dd41326f21a72&page={current_page}&pageSize=6'
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if not articles:  # No more articles available, reset to the first page
            current_page = 1  # Resetting page to 1 when out of articles
            return fetch_news()  # Recursive call to fetch the first page
        else:
            current_page += 1  # Prepare next page for the next request
            filtered_articles = [article for article in articles if article.get('urlToImage')]
            return jsonify({'articles': filtered_articles, 'status': 'ok', 'totalResults': len(filtered_articles)})
    else:
        return jsonify({'error': 'Failed to fetch news'}), response.status_code
    # url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=a4f7fdd20a1942b8bb0dd41326f21a72'
    # response = requests.get(url)
    # if response.status_code == 200:
    #     articles = response.json().get('articles', [])
    #     filtered_articles = [article for article in articles if article.get('urlToImage')]
    #     return jsonify({'articles': filtered_articles[:6], 'status': 'ok', 'totalResults': len(filtered_articles)})
    # else:
    #     return jsonify({'error': 'Failed to fetch news'}), response.status_code

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

    for description in liked_articles:

        keywords = extract_keywords(description)

        for keyword in keywords:

            if keyword in all_keywords.keys():

                all_keywords[keyword] += 1
            
            else:

                all_keywords[keyword] = 1

    sorted_items = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)
    most_common_keywords = [key for key, value in sorted_items[:3]]
    print("Dictionary: ", all_keywords)
    print("Most Common Keywords: ", most_common_keywords)

    return jsonify({'most_common_keywords': most_common_keywords}), 200

def extract_keywords(text):
    blob = TextBlob(text)
    return [phrase for phrase in blob.noun_phrases]

if __name__ == '__main__':
    app.run(debug=True)