from selenium import webdriver
from get_dir import pwd
p = pwd()
driver = p.get_firefox_driver()
driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()