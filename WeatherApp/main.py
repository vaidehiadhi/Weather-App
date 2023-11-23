import requests
import json
import os
city = input("Enter the name of the City\n ")

url = f"https://api.weatherapi.com/v1/current.json?key=d92594630c1e489eb12121507232311&q={city}"

r = requests.get(url)
print(r.text)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]
print(w)

os.system(f"say 'The current weather in {city} is {w} degrees' ")
