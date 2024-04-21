from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests
from collections import Counter
import re
import nltk
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

liked_articles = []
all_keywords = {}
used_articles = []
articles_accumulated = ['news', 'news', 'news']

@app.route('/news', methods=['GET'])
def fetch_news():
    num_articles_to_fetch = 10
    final_list = []

    for i in range(num_articles_to_fetch):
        print("inside 4 loop")
        keyword = None
        if (i >= 0) and (i <= 2):
            keyword = articles_accumulated[0]        
        elif (i >= 3) and (i <= 4):
            keyword = articles_accumulated[1]
        elif (i == 5):
            keyword = articles_accumulated[2]
        else:
            keyword = 'news'
        print("keyword is ", keyword)
        url = f'https://newsapi.org/v2/everything?q={keyword}&from=2024-03-22&sortBy=popularity&apiKey=YOUR_OWN_API'
        print("url is ", url)
        response = requests.get(url)
        print("response code is ", response.status_code)
        if response.status_code == 200:
            print("in if statement")
            articles = response.json().get('articles', [])
            filtered_articles = [article for article in articles if article.get('urlToImage', '') and article['title'] not in used_articles]
            final_list.append(filtered_articles[0])
            used_articles.append(filtered_articles[0]['title'])
        
    return jsonify({'articles': final_list, 'status': 'ok', 'totalResults': len(final_list)})

@app.route('/like', methods=['POST'])
def like_article():
    description = request.json.get('description')
    if description:
        liked_articles.append(description)
        return jsonify({'status': 'Description saved'}), 200
    else:
        return jsonify({'error': 'No description provided'}), 400

@app.route('/keywords', methods=['POST'])
def analyze_keywords():
    result = request.json.get('result')

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
    most_common_keywords = [key for key, _ in sorted_items[:3]]
    print("Dictionary: ", all_keywords)
    print("Most Common Keywords: ", most_common_keywords)

    articles_accumulated = most_common_keywords

    return jsonify({'updated': True}), 200

def extract_keywords(text):
    blob = TextBlob(text)
    return [phrase for phrase in blob.noun_phrases]

if __name__ == '__main__':
    app.run(debug=True)