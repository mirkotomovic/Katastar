from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, SoupStrainer
from bs import stripLinks, getAllData, saveCaptcha
from captcha_solver import solveCaptcha
import json
import re
import os
import pandas as pd
import time
import sys

df = pd.read_json("./data/katastarske_opstine.json")

# ovo je ok 150 KB tako da nebi trebalo da zajebava?
df = df.transpose()

# create a new Firefox session
driver = webdriver.Firefox()  # Postavi na hradless kad se reši captcha

data = {}

captchas_solved = 0
captchas_successful = 0
start_time = time.time()

skiped = 0

# Za svaku katastarsku opštinu
for starting_href, katOp in zip(df["href"], df["ImeKatOpstine"]):
    for parcelaID in range(0, 10000):
        base_img_url = "https://katastar.rgz.gov.rs/eKatastarPublic/"
        # create a new Firefox session
        # options = Options()
        # options.headless = True

        driver.get(base_img_url + starting_href)
        # Write parcela number

        inputElement = driver.find_element_by_id("ContentPlaceHolder1_txtBrParcele")
        inputElement.send_keys(parcelaID)
        
        while len(driver.find_elements_by_id("ContentPlaceHolder1_btnSubmit")) == 1:
            sys.stdout.write(f"\r {captchas_successful}/{captchas_solved}, Time:{time.time() - start_time}")

            captcha_img = driver.find_element_by_xpath(
                "//div[3]/div[1]/table/tbody/tr[3]/td/div/span[1]/img"
            ).get_attribute("src")
            captcha_img_path = "test_" + str(parcelaID) + ".jpg"

            saveCaptcha(captcha_img, captcha_img_path)

            captcha_solution = solveCaptcha(captcha_img_path)
            captchas_solved += 1
            captchaElement = driver.find_element_by_name(
                "ctl00$ContentPlaceHolder1$CaptchaControl"
            )
            captchaElement.send_keys(captcha_solution)
            time.sleep(4)
            driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()

        captchas_successful += 1

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
            # strainer = SoupStrainer("form")
            # print(href)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            data.update(getAllData(soup))
    with open("data/" + katOp + ".json", "w") as outfile:
        json.dump(data, outfile)


driver.quit()
