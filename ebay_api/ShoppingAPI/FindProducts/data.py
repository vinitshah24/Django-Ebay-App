import json
import os

json_file = os.path.join(os.path.dirname(__file__), 'products.json')

f = open(json_file, "r")
data = json.loads(f.read())

for index in range(len(data['Product'])):
    try:
        print(data['Product'][index]['DetailsURL'])
        if data['Product'][index]['ItemSpecifics']:
            info = data['Product'][index]['ItemSpecifics']
            # for p in range(len(info)):
            for p in range(len(info['NameValueList'])):
                print(
                    info['NameValueList'][p]['Name'] + ': ' +
                    info['NameValueList'][p]['Value'][0]
                )
        print(data['Product'][index]['StockPhotoURL'])
        print(data['Product'][index]['Title'])
        print('---------------------------------------------------')
    except Exception as e:
        pass
