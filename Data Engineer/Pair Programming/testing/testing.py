import requests

version = '1.0'
parameter = '1'
station = '53530'
ext = 'json'

r = requests.get(
    f"""https://opendata-download-metobs.smhi.se/api/version/{version}/parameter/{parameter}/station/{station}.{ext}""")

# print(json.dumps(r.json(), indent=4, sort_keys=True))

print(r)

print(r.json()['key'])
"""for item in r.json()['key']:
    print(item)

['station']:
    if item['name'] == "Hörby A":
        print(item['name'])
        for entry in item:
            print(entry)
            for a in entry:
                print(a)
"""
