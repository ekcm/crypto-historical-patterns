# https://alternative.me/crypto/fear-and-greed-index/

import requests 
import json

url = "https://api.alternative.me/fng/?limit=5000&format=json&date_format=us"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open('../notebooks/data/fear_and_greed.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
else:
    print("Failed fear and greed data extraction")