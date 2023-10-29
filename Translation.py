# import requests
#
# from pprint import pprint as print
#
# app_id = '62b446b5'
# app_key = 'c2fe6960887f53b88999a767283d7e34'
# language = 'en-gb'
#
# word_id = "python"
# url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
#
# r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# print(r.status_code)
# res = r.json()
# print(res)
#
# # print(res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
# # print(res["results"][0]["lexicalEntries"][0]["entries"][0]["pronunciations"][0]["audioFile"][0])


import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

a = input("Qaysi tilda yozasiz?: ")
b = input("Qaysi tilga tarjima qilib beri?: ")
c = input(f"Tanlagan {a}-da matn kiriting: ")

payload = {
	"q": c,
	"target": b,
	"source": a
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "f061a75850mshb954ddf57dbf5edp167995jsnc803cba4b462",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
res = response.json()
# print(res)
# print(res.keys())   oldin shu kod bn korvolamiz ichini
print(res['data']['translations'][0]['translatedText'])
# print(res["data"]["translations"]["translatedText"])
