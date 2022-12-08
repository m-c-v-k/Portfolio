#! python3

# Importing necessary libraries
import requests

r = requests.get("http://api.github.com")

print(f"Status code: {r.status_code}")
print(r.text)
