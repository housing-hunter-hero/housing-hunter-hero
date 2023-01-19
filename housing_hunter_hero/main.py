from housing_hunter import zip_scraper, bed_bath_scraper, smash_together, results_of_scrape
from graphics import greeting


def main():
	# greeting()
	results_of_scrape(smash_together(zip_scraper('06118'), bed_bath_scraper('06118')))


if __name__ == "__main__":
	main()
