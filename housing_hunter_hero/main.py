from housing_hunter import name_url_scraper, bed_bath_scraper, smash_together


def main():
	smash_together(name_url_scraper(), bed_bath_scraper())


if __name__ == "__main__":
	main()
