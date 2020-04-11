from dotenv import load_dotenv
import requests
import json
import os

api_url = ''
api_key = ''
env_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..\..\..', '.env')
)
load_dotenv(env_file)

metadata = {
    'callname': 'FindProducts',
    'appid': os.environ.get('PROD_APP_ID'),
    'version': '1119',
    'siteid': '0',
    'QueryKeywords': 'Macbook',
    'MaxEntries': '50',
    'responseencoding': 'JSON'
}

api_url = 'https://open.api.ebay.com/shopping'
response = requests.get(url=api_url, params=metadata)
if response.status_code == 200:
    parsed = response.json()
    with open('products.json', 'w+') as f:
        json.dump(parsed, f, indent=2, sort_keys=True)
else:
    print("Request Failed!")
