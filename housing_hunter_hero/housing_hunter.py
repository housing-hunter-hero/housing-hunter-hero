import requests
from bs4 import BeautifulSoup
import json

headers={'User-Agent': 'Mozilla/5.0'}
url = "https://www.redfin.com/city/16163/WA/Seattle"
response = requests.get(url, headers=headers)

# soup = BeautifulSoup(response.text, "html.parser")
# soup = soup.find_all('script')
#
# soup.pop(0)
#
# for sou in soup:
# 	return_me = json.loads(sou.string)
# 	print(return_me)

# print(soup)
# print(soup)
# soup = json.loads(soup[1].get_text())
# print(soup[0]['name'])
# susan = (soup[0]['url'])
# print(f"http://www.redfin.com/{susan}")



#
# # response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# a_links = soup.find_all('div', class_="homeAddressV2")
a_links = soup.find_all('div', class_="HomeStatsV2 font-size-small")
return_me = ""
# for i in a_links:
# 	return_me += i.text + " " + '\n'


for i in a_links:
	return_me += i.parent.text + " " + '\n'


# # return_me = return_me.replace("Beds", "Beds ")
# return_me = return_me.replace("Bed", "Bed ")
# return_me = return_me.replace("Bed s", "Beds ")
# # return_me = return_me.replace("Baths", "Baths ")
# return_me = return_me.replace("Bath", "Bath ")
# return_me = return_me.replace("Bath s", "Baths ")
print(return_me)
