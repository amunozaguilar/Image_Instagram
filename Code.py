from selenium import webdriver
from bs4 import BeautifulSoup
import urllib

userprofilename = input("Name Profile: ")
driver = webdriver.Chrome("PATH.../chromedriver.exe")

driver.get("https://www.instagram.com/" + userprofilename+ "/")

body = driver.find_element_by_tag_name("body")
profile = body.get_attribute("innerHTML")

soup = BeautifulSoup(profile, "html.parser")

userimagetag = soup.select('img[alt="' +userprofilename+ '\'s profile picture"]')
if not userimagetag:
    userimagetag = soup.select('.be6sR')
    print("Success Process")
    
urllib.request.urlretrieve(userimagetag[0]["src"],"userprofile.jpg")
driver.close()
