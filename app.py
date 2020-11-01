import requests
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def proxy():
    city = request.args.get('city')
    res = requests.get(f"https://npiregistry.cms.hhs.gov/api/?version=2.0&city={city}")
    resJson = res.json()
    return resJson

if __name__ == '__main__':
    app.run()