from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

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
        articles = response.json().get('articles', [])[:6]  # Limit to 6 articles
        return jsonify({'articles': articles, 'status': 'ok', 'totalResults': len(articles)})
    else:
        return jsonify({'error': 'Failed to fetch news'}), response.status_code

   # if response.status_code != 200:
   #     return jsonify({'error': 'Failed to fetch news'}), response.status_code
    
   # return jsonify(response.json())
    
if __name__ == '__main__':
    app.run(debug=True)