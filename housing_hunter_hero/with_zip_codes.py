import requests
from bs4 import BeautifulSoup
import json
import re


def zip_scraper(zip_):

	headers = {'User-Agent': 'Mozilla/5.0'}
	url = f'https://www.redfin.com/zipcode/{zip_}'
	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.text, "html.parser")
	soup = soup.find_all('script', type="application/ld+json")

	x = []
	for num in range(1, len(soup)):
		x.append(json.loads(soup[num].get_text()))

	purge_ = [elm for elm in x if isinstance(elm, list)]
	lst = [v for i, v in enumerate(purge_) if i % 2 == 0]
	while len(lst) > 10:
		lst.pop()
	bucket = []
	for item in lst:
		# print(type(item))
		bucket.append([item[0]['name'], item[1]['url']])
	return bucket


def bed_bath_scraper(zip_):

	headers = {'User-Agent': 'Mozilla/5.0'}
	url = f"https://www.redfin.com/zipcode/{zip_}"
	response = requests.get(url, headers=headers)

	soup_ = BeautifulSoup(response.text, "html.parser")
	a_links = soup_.find_all('div', class_="HomeStatsV2 font-size-small")
	return_b = []

	for i in a_links:
		return_b.append(i.text)
	for i in range(len(return_b)):
		return_b[i] = return_b[i].replace("Bed", "Bed ")
		return_b[i] = return_b[i].replace("Bed s", "Beds ")
		return_b[i] = return_b[i].replace("Bath", "Bath ")
		return_b[i] = return_b[i].replace("Bath s", "Baths ")

	return_me = []

	for i in a_links:
		return_me.append(i.parent.text)

	while len(return_me) > 10:
		return_me.pop()
	while len(return_b) > 10:
		return_b.pop()

	for i in range(len(return_me)):
		return_me[i] = return_me[i].replace("Bed", "Bed ")
		return_me[i] = return_me[i].replace("Bed s", "Beds ")
		return_me[i] = return_me[i].replace("Bath", "Bath ")
		return_me[i] = return_me[i].replace("Bath s", "Baths ")
		return_me[i] = return_me[i].replace(return_b[i], " "+return_b[i]+" ")

	for i in range(len(return_me)):
		return_me[i] = re.sub(r'Listing(.*)', '', return_me[i])

	return return_me


def smash_together(thing1, thing2):
	for i in range(len(thing2)):
		print(f"Property {i+1}: ", thing2[i], " - ", "\n ", f"https://www.redfin.com/{(thing1[i][1])}")
		print(" ")


if __name__ == "__main__":
	smash_together(zip_scraper('77008'), bed_bath_scraper('77008'))
	# print(zip_scraper('06118'))
	# print(bed_bath_scraper('11411'))
