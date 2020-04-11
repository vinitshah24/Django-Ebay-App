from dotenv import load_dotenv
import requests
import json
import os

api_url = ''
api_key = ''
env_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..\..', '.env')
)
load_dotenv(env_file)

# FILTER
metadata = {
    'OPERATION-NAME': 'findItemsByKeywords',
    'SECURITY-APPNAME': os.environ.get('PROD_APP_ID'),
    'SERVICE-VERSION': '1.0.0',
    'keywords': 'Macbook',
    'RESPONSE-DATA-FORMAT': 'JSON',
    'itemFilter.name': 'MaxPrice',
    'itemFilter.value': '500',
    'itemFilter.paramName': 'Currency',
    'itemFilter.paramValue': 'USD',
    'paginationInput.entriesPerPage': '20'
}

api_url = 'https://svcs.ebay.com/services/search/FindingService/v1'
response = requests.get(url=api_url, params=metadata)
if response.status_code == 200:
    parsed = response.json()
    with open('items.json', 'w+') as f:
        json.dump(parsed, f, indent=2, sort_keys=True)
else:
    print("Request Failed!")
