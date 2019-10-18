import requests
from random import randint

val = randint(1, 50)
print(val)
r = requests.get(f"https://swapi.co/api/people/{val}")

json = r.json()

print(json.get('name'))
