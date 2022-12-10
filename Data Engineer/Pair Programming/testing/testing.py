import requests
import json

r = requests.get(
    "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json")

#print(json.dumps(r.json(), indent=4, sort_keys=True))


# print(r.json()['timeSeries'])
for item in r.json()['timeSeries']:
    print(item['validTime'])
    for entry in item['parameters']:
        print(entry)
