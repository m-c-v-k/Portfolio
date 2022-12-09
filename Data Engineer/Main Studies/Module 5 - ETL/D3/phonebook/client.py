import requests

data = {"entry": {
    "name": "Jakob Rolandsson",
    "number": "0725080995",
    "address": "Häraldsvägen 3B"
}}


#r = requests.post("http://127.0.0.1:5000/phonebook", json=data)

r = requests.get("http://127.0.0.1:5000/phonebook")

for entry in r.json():
    print(entry["name"], entry["number"], "-", entry["address"], "\n")

requests.delete("http://127.0.0.1:5000/phonebook/name/Norma%20Fisher")
print(requests.get("http://127.0.0.1:5000/phonebook/name/Norma%20Fisher"))
