import requests
from bs4 import BeautifulSoup
import json
import re


def zip_scraper(zip_):
	"""
	A function which will access redfin.com and use a user input zip code to gather
	relevant info handled inside a JSON
	:param zip_: 5-digit zip code
	:return: a list of properties
	"""
	headers = {'User-Agent': 'Mozilla/5.0'}
	url = f'https://www.redfin.com/zipcode/{zip_}'
	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.text, "html.parser")
	soup = soup.find_all('script', type="application/ld+json")
	bucket = []
	x = []
	for num in range(1, len(soup)):
		x.append(json.loads(soup[num].get_text()))

	purge_ = [elm for elm in x if isinstance(elm, list)]
	lst = [v for i, v in enumerate(purge_) if i % 2 == 0]
	while len(lst) > 15:
		lst.pop()

	for item in lst:
		# print(type(item))
		bucket.append([item[0]['name'].replace(zip_, ""), item[1]['url']])
	return bucket


def bed_bath_scraper(zip_):
	"""
	A function which will access redfin.com and use a user input zip code to gather
	relevant info stored inside the HTML code
	:param zip_: 5-digit zip code
	:return: a list of properties
	"""
	bucket = zip_scraper(zip_)
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

	while len(return_me) > 15:
		return_me.pop()
	while len(return_b) > 15:
		return_b.pop()

	for i in range(len(return_me)):
		return_me[i] = return_me[i].replace("Bed", "Bed ")
		return_me[i] = return_me[i].replace("Bed s", "Beds ")
		return_me[i] = return_me[i].replace("Bath", "Bath ")
		return_me[i] = return_me[i].replace("Bath s", "Baths ")
		return_me[i] = return_me[i].replace(return_b[i], " " + return_b[i] + " ")

	for i in range(len(return_me)):
		return_me[i] = re.sub(r'Listing(.*)', '', return_me[i])

	for i in range(len(return_me)):
		return_me[i] = re.sub(f"{zip_}(.*)", '', return_me[i])

	return return_me


def smash_together(list_1, list_2):
	"""
	Combines two property lists based on the address of the property
	:param list_1: an output from zip_scraper
	:param list_2: an output from bed_bath_scraper
	:return: a list of properties to be displayed to the user
	"""
	while list_2:
		for x in range(len(list_1)):
			if list_2[0].endswith(list_1[x][0]):
				list_1[x].append(list_2[0])
		list_2.pop(0)
	results = []
	for i in list_1:
		if len(i) >= 3:
			results.append(i)

	return results


def results_of_scrape(scraped_data):
	"""
	Parses a list into user digestible information
	:param scraped_data: a list output from smash_together
	:return: a list of results and a print to the console of the same list
	"""
	results = ""
	for i in range(len(scraped_data)):
		results += f"Property {i + 1}: {scraped_data[i][2]} \n URL: https://www.redfin.com{scraped_data[i][1]} \n"
		results += "\n"
	print(results)
	return results


def user_zip():
	"""
	A function which handles the request for zip code from the user
	:return: returns the results_of_scrape to the user based on their
	input of a zipcode
	"""
	user_input = input('> ')
	results_of_scrape((smash_together(zip_scraper(user_input), bed_bath_scraper(user_input))))


if __name__ == "__main__":
	user_zip()
