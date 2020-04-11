from datetime import datetime
import json
import os

def formatTime(time_date):
    formatted_dt = datetime.strptime(time_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_dt.strftime('%I:%M %p')

def formatDate(time_date):
    formatted_dt = datetime.strptime(time_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_dt.strftime('%Y-%m-%d')

json_file = os.path.join(os.path.dirname(__file__), 'items.json')
f = open(json_file, "r")
data = json.loads(f.read())
results_count = int(
    data['findItemsByKeywordsResponse'][0]['searchResult'][0]['@count']
)
items = data['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']
for i in range(results_count):
    print("Item Condition: " + items[i]['condition'][0]['conditionDisplayName'][0])
    print("Image URL: " + items[i]['galleryURL'][0])
    print("Item ID: " + items[i]['itemId'][0])
    print("Best Offer Available: " + items[i]['listingInfo'][0]['bestOfferEnabled'][0])
    print("Buy it Now Available: " + items[i]['listingInfo'][0]['buyItNowAvailable'][0])
    start_datetime = items[i]['listingInfo'][0]['startTime'][0]
    print("Listing Start Date: " + formatDate(start_datetime))
    print("Listing Start Time: " + formatTime(start_datetime))
    end_datetime = items[i]['listingInfo'][0]['endTime'][0]
    print("Listing End Date: " + formatDate(end_datetime))
    print("Listing End Time: " + formatTime(end_datetime))
    print("Category ID: " + items[i]['primaryCategory'][0]['categoryId'][0])
    print("Category Name: " + items[i]['primaryCategory'][0]['categoryName'][0])
    print("Returns Accepted: " + items[i]['returnsAccepted'][0])
    print("Auction Current Price: " + 
    items[i]['sellingStatus'][0]['convertedCurrentPrice'][0]['@currencyId'] + " " + 
    items[i]['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']
    )
    print("Selling Status: " + items[i]['sellingStatus'][0]['sellingState'][0])
    print("Title: " + items[i]['title'][0])
    if not (items[i].get('subtitle') is None):
        print("Subtitle: " + items[i]['subtitle'][0])
    print("Item URL: " + items[i]['viewItemURL'][0])
    print("-----------------------------------------------------------------------------------------")
