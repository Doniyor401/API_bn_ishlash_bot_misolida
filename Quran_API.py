import requests
from pprint import pprint as print

sura = 1
oyat = 4
tafsir = 'uzb-muhammadsodikmu'

url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
r = requests.get(url_sura)
# print(r.status_code)

url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
r1 = requests.get(url_oyat)
print(r1.status_code)


print(r1.json()['text'])