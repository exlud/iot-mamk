import urequests
import json

number = int(input("Number of Pokemon: "))
api = f"https://pokeapi.co/api/v2/pokemon-species/{number}"
response = urequests.get(api)

if response.status_code == 200:
    data = json.loads(response.text)
    name = data.get('name')
    print("Name of Pokemon ", number, ": ", name)
else:
    print("Network error with code:", response.status_code)

response.close()
