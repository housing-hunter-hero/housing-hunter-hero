import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.redfin.com/city/16163/WA/Seattle"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
soup = soup.find_all('script', type="application/ld+json")

x = []
for num in range(1, len(soup)):
	x.append(json.loads(soup[num].get_text()))

lst = [v for i, v in enumerate(x) if i % 2 == 0]
# print(lst)
while len(lst) > 8:
	lst.pop()
bucket = []
for item in lst:
	bucket.append([item[0]['name'], item[1]['url']])
# 	# bucket.append([item[0][0]['name'], f"https://www.redfin.com/{item[0][1]['url']}"])
# # name_bucket = lst[0][0]['name']
# # price_bucket = lst[0][1]['offers']['price']
# # url_bucket = f"https://www.redfin.com/{lst[0][1]['url']}"

print(f"https://www.redfin.com/{(bucket[0][1])}")

soup_ = BeautifulSoup(response.text, "html.parser")
# a_links = soup.find_all('div', class_="homeAddressV2")
a_links = soup_.find_all('div', class_="HomeStatsV2 font-size-small")
return_me = ""
return_b = []
# just the beds, baths, sqft
for i in a_links:
	return_b.append(i.text)
for i in range(len(return_b)):
	return_b[i] = return_b[i].replace("Bed", "Bed ")
	return_b[i] = return_b[i].replace("Bed s", "Beds ")
	return_b[i] = return_b[i].replace("Bath", "Bath ")
	return_b[i] = return_b[i].replace("Bath s", "Baths ")
# print(return_b)
return_me = []
# all that and then some
for i in a_links:
	return_me.append(i.parent.text)

while len(return_me) > 8:
	return_me.pop()
while len(return_b) > 8:
	return_b.pop()

for i in range(len(return_me)):
	return_me[i] = return_me[i].replace("Bed", "Bed ")
	return_me[i] = return_me[i].replace("Bed s", "Beds ")
	return_me[i] = return_me[i].replace("Bath", "Bath ")
	return_me[i] = return_me[i].replace("Bath s", "Baths ")
	return_me[i] = return_me[i][:-(25+len(bucket[i][0]))]
	return_me[i] = return_me[i].replace(return_b[i], " "+return_b[i]+" ")

print("")
print("")

for i in range(len(return_me)):
	print(f"Property {i+1}: ", return_me[i], " - ", f"https://www.redfin.com/{(bucket[i][1])}")
	print(" ")

