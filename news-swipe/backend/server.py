from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
@app.route('/news', methods=['GET'])

def main():
    
    # url = ('https://newsapi.org/v2/everything?'
    #    'q=Mario&'
    #    'from=2024-04-19&'
    #    'sortBy=popularity&'
    #    'apiKey=a4f7fdd20a1942b8bb0dd41326f21a72')
    
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=a4f7fdd20a1942b8bb0dd41326f21a72')
    
    response = requests.get(url)
    if response.status_code == 200:

        articles = response.json().get('articles', [])
        filtered_articles = filter_articles(articles)
        filtered_articles = filtered_articles[:6]

        return jsonify({'articles': filtered_articles, 'status': 'ok', 'totalResults': len(filtered_articles)})
    
    else:
    
        return jsonify({'error': 'Failed to fetch news'}), response.status_code

def filter_articles(articles):

    processed_articles = []

    for article in articles:

        if article.get('urlToImage', ''):

            processed_articles.append(article)

    return processed_articles
    
if __name__ == '__main__':
    app.run(debug=True)