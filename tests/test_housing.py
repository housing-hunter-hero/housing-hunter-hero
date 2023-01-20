import pytest
from housing_hunter_hero.housing_hunter import zip_scraper, bed_bath_scraper, smash_together, results_of_scrape, user_zip


# @pytest.mark.skip("TODO")
def test_exists_zip_scraper():
    assert zip_scraper('06118')


# @pytest.mark.skip("TODO")
def test_zip_scraper_is_working():
    zip_ = '21222'
    actual = zip_scraper(zip_)
    expected = [['120 Bayside Dr, Dundalk, MD ', '/MD/Dundalk/120-Bayside-Dr-21222/home/9333067'], ['836 Jeannette Ave, Dundalk, MD ', '/MD/Dundalk/836-Jeannette-Ave-21222/home/9334910'], ['2900 Page Dr, Dundalk, MD ', '/MD/Dundalk/2900-Page-Dr-21222/home/9347443'], ['3702 N Point Rd, Dundalk, MD ', '/MD/Dundalk/3702-N-Point-Rd-21222/home/9470262'], ['3406 Dunran Rd, Dundalk, MD ', '/MD/Dundalk/3406-Dunran-Rd-21222/home/9342643'], ['1614 Gray Haven Ct, Dundalk, MD ', '/MD/Dundalk/1614-Gray-Haven-Ct-21222/home/9331817'], ['1246 Delbert Ave, Baltimore City, MD ', '/MD/Baltimore/1246-Delbert-Ave-21222/home/11062805'], ['1907 Jefferson Rd, Dundalk, MD ', '/MD/Baltimore/1907-Jefferson-Rd-21222/home/9298328'], ['7148 Martell Ave, Dundalk, MD ', '/MD/Dundalk/7148-Martell-Ave-21222/home/9296636'], ['9 N Dundalk Ave, Dundalk, MD ', '/MD/Baltimore/9-N-Dundalk-Ave-21222/home/9329327'], ['600 Willow Spring Rd, Dundalk, MD ', '/MD/Dundalk/600-Willow-Spring-Rd-21222/home/12536361'], ['6918 Homeway, Dundalk, MD ', '/MD/Dundalk/6918-Homeway-21222/home/9297127'], ['7908 Wallace Rd, Dundalk, MD ', '/MD/Dundalk/7908-Wallace-Rd-21222/home/9315638'], ['1947 Walnut Ave, Dundalk, MD ', '/MD/Dundalk/1947-Walnut-Ave-21222/home/9343663'], ['7831 Saint Claire Ln, Dundalk, MD ', '/MD/Dundalk/7831-St-Claire-Ln-21222/home/9464119']]

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exists_bed_bath_scraper():
    assert bed_bath_scraper('11790')


# @pytest.mark.skip("TODO")
def test_bed_bath_scraper_is_working():
    zip_ = '21222'
    actual = bed_bath_scraper(zip_)
    expected = ['$219,900 3 Beds 1.5 Baths 1,188 Sq. Ft. 120 Bayside Dr, Dundalk, MD ', '$140,000 2 Beds 1 Bath 812 Sq. Ft. 203 Chestnut St, Dundalk, MD ', '$164,900 3 Beds 1.5 Baths 1,024 Sq. Ft. 836 Jeannette Ave, Dundalk, MD ', '$300,000 4 Beds 2 Baths 1,908 Sq. Ft. 206 German Hill Rd, Dundalk, MD ', '$235,995 3 Beds 1 Bath 825 Sq. Ft. 2900 Page Dr, Dundalk, MD ', '$179,990 3 Beds 1.5 Baths 1,258 Sq. Ft. 2020 Dineen, Dundalk, MD ', '$240,000 5 Beds 3 Baths 1,624 Sq. Ft. 3702 N Point Rd, Dundalk, MD ', '$210,000 2 Beds 1 Bath 768 Sq. Ft. 6915 Homeway, Baltimore, MD ', '$165,000 2 Beds 1.5 Baths 1,120 Sq. Ft. 3406 Dunran Rd, Dundalk, MD ', '$255,000 3 Beds 2 Baths 1,426 Sq. Ft. 39 Mavista Ave, Dundalk, MD ', '$229,900 3 Beds 2 Baths 1,258 Sq. Ft. 1614 Gray Haven Ct, Dundalk, MD ', '$299,900 3 Beds 1.5 Baths 1,984 Sq. Ft. 1703 Pinewood Dr, Dundalk, MD ', '$75,000 3 Beds 1 Bath 1,024 Sq. Ft. 1246 Delbert Ave, Baltimore City, MD ', '$179,999 2 Beds 1 Bath 1,066 Sq. Ft. 8049 Wallace Rd, Dundalk, MD ', '$249,900 3 Beds 2 Baths 1,238 Sq. Ft. 1907 Jefferson Rd, Dundalk, MD ']

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exists_smash_together():
    assert smash_together(zip_scraper('06118'), bed_bath_scraper('06118'))


# @pytest.mark.skip("TODO")
def test_smash_together_is_working():
    zip_1 = [['120 Bayside Dr, Dundalk, MD ', '/MD/Dundalk/120-Bayside-Dr-21222/home/9333067'], ['3702 N Point Rd, Dundalk, MD ', '/MD/Dundalk/3702-N-Point-Rd-21222/home/9470262'], ['3406 Dunran Rd, Dundalk, MD ', '/MD/Dundalk/3406-Dunran-Rd-21222/home/9342643'], ['206 German Hill Rd, Dundalk, MD ', '/MD/Dundalk/206-German-Hill-Rd-21222/home/9346432'], ['1614 Gray Haven Ct, Dundalk, MD ', '/MD/Dundalk/1614-Gray-Haven-Ct-21222/home/9331817'], ['1703 Pinewood Dr, Dundalk, MD ', '/MD/Dundalk/1703-Pinewood-Dr-21222/home/9318661'], ['8049 Wallace Rd, Dundalk, MD ', '/MD/Dundalk/8049-Wallace-Rd-21222/home/9451492'], ['6508 Cleveland Ave, Baltimore, MD ', '/MD/Baltimore/6508-Cleveland-Ave-21222/home/11067031'], ['2700 Mccomas Ave, Dundalk, MD ', '/MD/Dundalk/2700-McComas-Ave-21222/home/9293702'], ['1927 Codd, Dundalk, MD ', '/MD/Dundalk/1927-Codd-Ave-21222/home/9338544'], ['1725 Stokesley Rd, Dundalk, MD ', '/MD/Dundalk/1725-Stokesley-Rd-21222/home/9332276'], ['1761 Brookview Rd, Dundalk, MD ', '/MD/Dundalk/1761-Brookview-Rd-21222/home/9349192'], ['6824 Dunbar Rd, Dundalk, MD ', '/MD/Dundalk/6824-Dunbar-Rd-21222/home/9328989'], ['104 Shipway, Dundalk, MD ', '/MD/Dundalk/104-Shipway-21222/home/9339780'], ['1947 Walnut Ave, Dundalk, MD ', '/MD/Dundalk/1947-Walnut-Ave-21222/home/9343663']]
    zip_2 = ['$219,900 3 Beds 1.5 Baths 1,188 Sq. Ft. 120 Bayside Dr, Dundalk, MD ', '$164,900 3 Beds 1.5 Baths 1,024 Sq. Ft. 836 Jeannette Ave, Dundalk, MD ', '$240,000 5 Beds 3 Baths 1,624 Sq. Ft. 3702 N Point Rd, Dundalk, MD ', '$210,000 2 Beds 1 Bath 768 Sq. Ft. 6915 Homeway, Baltimore, MD ', '$165,000 2 Beds 1.5 Baths 1,120 Sq. Ft. 3406 Dunran Rd, Dundalk, MD ', '$255,000 3 Beds 2 Baths 1,426 Sq. Ft. 39 Mavista Ave, Dundalk, MD ', '$300,000 4 Beds 2 Baths 1,908 Sq. Ft. 206 German Hill Rd, Dundalk, MD ', '$179,990 3 Beds 1.5 Baths 1,258 Sq. Ft. 2020 Dineen, Dundalk, MD ', '$229,900 3 Beds 2 Baths 1,258 Sq. Ft. 1614 Gray Haven Ct, Dundalk, MD ', '$235,995 3 Beds 1 Bath 825 Sq. Ft. 2900 Page Dr, Dundalk, MD ', '$299,900 3 Beds 1.5 Baths 1,984 Sq. Ft. 1703 Pinewood Dr, Dundalk, MD ', '$75,000 3 Beds 1 Bath 1,024 Sq. Ft. 1246 Delbert Ave, Baltimore City, MD ', '$179,999 2 Beds 1 Bath 1,066 Sq. Ft. 8049 Wallace Rd, Dundalk, MD ', '$249,900 3 Beds 2 Baths 1,238 Sq. Ft. 1907 Jefferson Rd, Dundalk, MD ', '$140,000 4 Beds 2.5 Baths 2,036 Sq. Ft. 6508 Cleveland Ave, Baltimore, MD ']
    actual = smash_together(zip_1, zip_2)
    expected = [['120 Bayside Dr, Dundalk, MD ', '/MD/Dundalk/120-Bayside-Dr-21222/home/9333067', '$219,900 3 Beds 1.5 Baths 1,188 Sq. Ft. 120 Bayside Dr, Dundalk, MD '], ['3702 N Point Rd, Dundalk, MD ', '/MD/Dundalk/3702-N-Point-Rd-21222/home/9470262', '$240,000 5 Beds 3 Baths 1,624 Sq. Ft. 3702 N Point Rd, Dundalk, MD '], ['3406 Dunran Rd, Dundalk, MD ', '/MD/Dundalk/3406-Dunran-Rd-21222/home/9342643', '$165,000 2 Beds 1.5 Baths 1,120 Sq. Ft. 3406 Dunran Rd, Dundalk, MD '], ['206 German Hill Rd, Dundalk, MD ', '/MD/Dundalk/206-German-Hill-Rd-21222/home/9346432', '$300,000 4 Beds 2 Baths 1,908 Sq. Ft. 206 German Hill Rd, Dundalk, MD '], ['1614 Gray Haven Ct, Dundalk, MD ', '/MD/Dundalk/1614-Gray-Haven-Ct-21222/home/9331817', '$229,900 3 Beds 2 Baths 1,258 Sq. Ft. 1614 Gray Haven Ct, Dundalk, MD '], ['1703 Pinewood Dr, Dundalk, MD ', '/MD/Dundalk/1703-Pinewood-Dr-21222/home/9318661', '$299,900 3 Beds 1.5 Baths 1,984 Sq. Ft. 1703 Pinewood Dr, Dundalk, MD '], ['8049 Wallace Rd, Dundalk, MD ', '/MD/Dundalk/8049-Wallace-Rd-21222/home/9451492', '$179,999 2 Beds 1 Bath 1,066 Sq. Ft. 8049 Wallace Rd, Dundalk, MD '], ['6508 Cleveland Ave, Baltimore, MD ', '/MD/Baltimore/6508-Cleveland-Ave-21222/home/11067031', '$140,000 4 Beds 2.5 Baths 2,036 Sq. Ft. 6508 Cleveland Ave, Baltimore, MD ']]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exists_results_of_scrape():
    assert results_of_scrape(smash_together(zip_scraper('06118'), bed_bath_scraper('06118'))) != ""


# @pytest.mark.skip("TODO")
def test_exists_user_zip():
    assert user_zip() != ""


# @pytest.mark.skip("TODO")
def test_user_zip_is_working():
    pass

