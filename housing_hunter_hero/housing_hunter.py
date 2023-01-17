import requests
from bs4 import BeautifulSoup
import json

headers={'User-Agent': 'Mozilla/5.0'}
url = "https://www.redfin.com/city/16163/WA/Seattle"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
soup = soup.find_all('script', type="application/ld+json")

# commented out to return bottom to before
# soup = json.loads(soup[1].get_text())
# print(soup)
# print(soup[1])
# print(soup[1]['offers']['price'])
# susan = (soup[0]['url'])
#
# print(f"http://www.redfin.com/{susan}")


soup = BeautifulSoup(response.text, "html.parser")
# a_links = soup.find_all('div', class_="homeAddressV2")
a_links = soup.find_all('div', class_="HomeStatsV2 font-size-small")
return_me = ""

# just the beds, baths, sqft
# for i in a_links:
# 	return_me += i.text + " " + '\n'

# all that and then some
for i in a_links:
	return_me += i.parent.text + " " + '\n'


return_me = return_me.replace("Bed", "Bed ")
return_me = return_me.replace("Bed s", "Beds ")
return_me = return_me.replace("Bath", "Bath ")
return_me = return_me.replace("Bath s", "Baths ")
print(return_me)
