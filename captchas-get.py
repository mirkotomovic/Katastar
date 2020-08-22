from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
from bs import stripLinks, getAllData, saveCaptcha, getCaptchaDataToSave
import json
import re
import os
import pandas as pd
import time

df = pd.read_json("./data/katastarske_opstine.json")

# ovo je ok 150 KB tako da nebi trebalo da zajebava?
df = df.transpose()

# create a new Firefox session
driver = webdriver.Firefox()  # Postavi na hradless kad se reši captcha

data = {}
# Za svaku katastarsku opštinu
for starting_href in df["href"]:
    for parcelaID in range(3, 5):
        base_img_url = "https://katastar.rgz.gov.rs/eKatastarPublic/"
        # create a new Firefox session
        # options = Options()
        # options.headless = True

        driver.get(base_img_url + starting_href)
        # Write parcela number

        inputElement = driver.find_element_by_id("ContentPlaceHolder1_txtBrParcele")
        inputElement.send_keys(parcelaID)
        while len(driver.find_elements_by_id("ContentPlaceHolder1_btnSubmit")) == 1:
            time.sleep(5)

            # Ispod je deo vezan za captchu ovo sa fajlom je da bi ja mogau ručno da je rešim...
            captcha_img = driver.find_element_by_xpath(
                "//div[3]/div[1]/table/tbody/tr[3]/td/div/span[1]/img"
            ).get_attribute("src")
            captcha_data = getCaptchaDataToSave(captcha_img)
            captcha_solution = input().strip()

            captchaElement = driver.find_element_by_name(
                "ctl00$ContentPlaceHolder1$CaptchaControl"
            )
            captchaElement.send_keys(captcha_solution)

            driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
        with open("./captchas/" + captcha_solution + ".jpg", "wb") as f:
            f.write(captcha_data)


driver.quit()

