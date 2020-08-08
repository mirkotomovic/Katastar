from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import re
import os
from bs import *

# launch url
starting_url = "https://katastar.rgz.gov.rs/eKatastarPublic/PublicAccess.aspx"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(starting_url)

html = driver.page_source
soup = BeautifulSoup(html)

opstina_ids = getOpstinasId(soup)

katOpstine = {}
for id in opstina_ids:
    driver.find_element_by_xpath(
        "//select[@name='ctl00$ContentPlaceHolder1$getOpstinaKO$dropOpstina']/option[@value='"
        + str(id)
        + "']"
    ).click()
    html = driver.page_source
    soup = BeautifulSoup(html)
    katOpstine.update(getKatOpstinas(soup))

with open("katastarske_opstine.json", "w") as outfile:
    json.dump(katOpstine, outfile)

driver.quit()
