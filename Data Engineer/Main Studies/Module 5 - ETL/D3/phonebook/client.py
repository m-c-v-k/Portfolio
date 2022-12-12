import requests

data = {"entry": {
    "name": "Jakob Rolandsson",
    "number": "0725080995",
    "address": "Häraldsvägen 3B",
    "added": "2018-02-12"
}}


r = requests.post("http://127.0.0.1:5000/phonebook", json=data)

#r = requests.get("http://127.0.0.1:5000/phonebook")


r = requests.get("http://127.0.0.1:5000/phonebook/")

"""for entry in r.json():
    print(entry["name"], entry["number"], "-", entry["address"], "\n")
"""
# requests.delete("http://127.0.0.1:5000/phonebook/name/Norma%20Fisher")
"""
r = requests.get("http://127.0.0.1:5000/phonebook/name/Norma%20Fisher")

for entry in r.json():
    print(entry["name"], entry["number"], "-", entry["address"], "\n")
"""
