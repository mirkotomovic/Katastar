from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
from bs import stripLinks, getAllData, saveCaptcha
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
            time.sleep(8)

            # Ispod je deo vezan za captchu ovo sa fajlom je da bi ja mogau ručno da je rešim...
            captcha_img = driver.find_element_by_xpath(
                "//div[3]/div[1]/table/tbody/tr[3]/td/div/span[1]/img"
            ).get_attribute("src")
            saveCaptcha(captcha_img, "test_" + str(parcelaID) + ".jpg")

            # captchaElement = driver.find_element_by_name(
            #     "ctl00$ContentPlaceHolder1$CaptchaControl"
            # )
            # captchaElement.send_keys(captcha_solution)

            driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()

        page = 2  # br prvog linka koji treba da klikne ukoliko link postoji
        grid = 1  # Br prve podparcele koju treba da klikne
        urls = set()
        while True:
            while True:
                html = driver.page_source
                strainer = SoupStrainer("center")
                soup = BeautifulSoup(html, "html.parser", parse_only=strainer)
                urls.update(stripLinks(soup))
                try:
                    driver.find_element_by_id(
                        "ContentPlaceHolder1_GridView1_cmdSelect_" + str(grid)
                    ).click()
                except:
                    break
                grid += 1
                if grid == 5:
                    grid = 0
                    break

            if page == 11:
                try:
                    driver.find_element_by_partial_link_text("..").click()
                except:
                    break
            elif page % 10 == 1:
                try:
                    driver.find_element_by_xpath("//table/tbody/tr/td[12]/a").click()
                except:
                    break
            else:
                try:
                    driver.find_element_by_partial_link_text(str(page)).click()
                except:
                    break
            page += 1

        for href in urls:
            driver.get(href)
            strainer = SoupStrainer("form")
            soup = BeautifulSoup(driver.page_source, "html.parser", parse_only=strainer)
            data.update(getAllData(soup))
    break


driver.quit()


with open("test.json", "w") as outfile:
    json.dump(data, outfile)
