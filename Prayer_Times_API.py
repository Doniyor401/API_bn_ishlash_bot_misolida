import requests
from pprint import pprint as print

city='tashkent'

url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=5"
r = requests.get(url)
print(r.status_code)

res = r.json()
print(res['results']['datetime'][0]['times'])

# print(f"Shom namozi vaqti: {res['results']['datetime'][0]['times']['Maghrib']}")
