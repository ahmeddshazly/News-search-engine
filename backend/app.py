from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os 
import requests

app = Flask(__name__)
CORS(app)

@app.route('/search',methods=["GET"])
def search():
    
    query = request.args.get('query')
    language=request.args.get('language')
    apiKey=os.getenv("api_key")
    url = 'https://newsapi.org/v2/everything?q=' + query + '&language=' + language +'&apiKey=' + apiKey
    response = requests.get(url)
    response= jsonify(response.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return (response)

if __name__ == '__main__':
    app.run(debug=True)