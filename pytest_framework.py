import pytest
from selenium.webdriver.common.keys import Keys

from get_dir import pwd


# to generate html report use pytest -v -s --html=report.html --self-contained-html Emission_Api_Test.py

def test_pytest():
    p = pwd()
    driver = p.get_firefox_driver()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def test_google():
    p = pwd()
    driver = p.get_firefox_driver()
    driver.get("http://google.com/")
    print("Headless Firefox Initialized")
    driver.quit()
