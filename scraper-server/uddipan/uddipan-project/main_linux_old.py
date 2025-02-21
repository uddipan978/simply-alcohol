from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
from allLinks import *
import pandas as pd
import pymysql
import openpyxl
import requests
import datetime
import json
import time
import os

# ------------------------------------------

# Global -

finalData_1 = []
finalData_2 = []
finalData_3 = []
finalData_4 = []
finalData_5 = []
finalData_6 = []
finalData_7 = []
finalData_8 = []
finalData_9 = []
finalData_10 = []
finalData_11 = []
finalData_11 = []
finalData_12 = []
finalData_13 = []
finalData_14 = []
finalData_15 = []
finalData_16 = []
finalData_17 = []
finalData_18 = []
finalData_19 = []
finalData_20 = []
finalData_21 = []
finalData_22 = []

print("--------------------------------------------")

print("Web Scrapper Started Successfully ...")
ct = datetime.datetime.now()
print("Start Time :-", ct)

print("--------------------------------------------")


CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# ------------------------------------------

# All Functions -

#-------------------------------------------------------------------------------------

# Functions for Site 1 - "https://cellarbration.com.sg/" -

def age_verification_1():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="agree-button"]')))
    driver.find_element(By.XPATH, '//button[@class="agree-button"]').click()
    time.sleep(5)


def get_info_1(url):
    driver.get(url)

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[1]/h1/span'))
        )
        productName2  = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[4]/td').text.replace("ml", "").replace("8 X ", "").replace("4cans x ", "").replace("4 x ", "")
        volume = int(volume_tc) / 10
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[5]/td').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[3]/div[1]/span[2]/span/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Cellarbration",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_1.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 2 - "https://cellarbration.com.sg/" -

def age_verification_2():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-radio-2"]/label/div[2]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mat-button"]')))
    driver.find_element(By.XPATH, '//*[@id="mat-radio-2"]/label/div[2]').click()
    e = driver.find_element(By.XPATH, '//button[@class="mat-button"]')
    loc = e.location
    print(loc)
    elem = driver.find_element(By.XPATH, '//button[@class="mat-button"]')
    ac = ActionChains(driver)
    ac.move_by_offset(434, 435).click().perform()
    time.sleep(5)


def get_info_2(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/h4'))
        )
        productName2 = productName2.text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").split(" ")
        volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/main/div/div[1]/div[1]/a[3]').text
        catagory = catagory.split(",") and catagory.split(" ")
        catagory = catagory[1]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/h3').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcohaul",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_2.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 3 - "https://cellarbration.com.sg/" -

def age_verification_3():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="validation_yes"]')))
    driver.find_element(By.XPATH, '//*[@id="validation_yes"]').click()


def get_info_3(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/h3'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").split(" ")
        # volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/app-root/div/app-singleproduct/div/div/div/div[2]/div[2]/p[1]').text
        catagory = catagory.split(",") and catagory.split(" ")
        catagory = catagory[1]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/ul[2]/li/div').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '// *[ @ id = "product-price-2876"] / span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcoholporter",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_3.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 4 - "https://cellarbration.com.sg/" -

def age_verification_4():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalWine"]/div/div/div/div[1]/div/div[1]/div/form/input')))
    driver.find_element(By.XPATH, '//*[@id="modalWine"]/div/div/div/div[1]/div/div[1]/div/form/input').click()


def get_info_4(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[2]/h3'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = productName2.replace("cl", "").replace("ml", "").split(" ")
        volume = volume_tc[-1]
        try:
            volume = int(volume) / 10
        except:
            volume = volume_tc[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li/div').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Bottels & Bottels",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_4.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 5 - "https://cellarbration.com.sg/" -s


def get_info_5(url):
    driver.get(url)

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-page"]/div[2]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/p').text.replace("ml", "").replace("8 X ", "").replace("4cans x ", "").replace("4 x ", "")
        volume = int(volume_tc) / 10
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[4]/span/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[1]/div[1]/span').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="product-page"]/div[2]/div[1]/div[1]/ins/span').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "chuansenghuat",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_5.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 6 - "https://cellarbration.com.sg/" -

def age_verification_6():
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_info_6(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-info-content"]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="data-size"]').text.replace("CTL", "")
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="content"]/h2').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-info-content"]/div[2]/div').text
        price = price.replace("$", "")
    except:
        print("Price not found for - ", url)

    tempV = {
        "Site": "coldstorage",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_6.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 7 - "https://cellarbration.com.sg/" -

def age_verification_7():
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_info_7(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section[3]/div/div/div[2]/div[1]/h3'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[7]/div[1]/div[1]/div/div[11]').text
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[7]/div[1]/div[1]/div/div[5]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[2]/div[3]/div[1]/div[1]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="amount"]').text
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "cornerstonewines",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_7.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 8 - "https://cellarbration.com.sg/" -

def age_verification_8():
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_info_8(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        pass
        # volume_1 = productName2.split(" ")
        # volume = volume_1[-1]
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div[1]/div/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "getit",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_8.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 9 - "https://cellarbration.com.sg/" -

def age_verification_9():
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]')))
    driver.find_element(By.XPATH, '//*[@id="ematic_closeExitIntentOverlay_2_xl_1_2"]').click()


def get_info_9(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product-info-content"]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="data-size"]').text
        volume = volume.replace("CTL", "")
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="blade-app"]/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div[1]/div/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="product-info-content"]/div[2]/div').text
        price = price.replace("$", "")
    except:
        print("Price not found for - ", url)

    tempV = {
        "Site": "giant",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_9.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 10 - "https://cellarbration.com.sg/" -

def age_verification_10():
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="close-icon"]')))
    driver.find_element(By.XPATH, '//*[@id="close-icon"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]')))
    driver.find_element(By.XPATH, '//*[@id="agp_row"]/div/div/div[3]/div/form[1]').click()


def get_info_10(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[2]/td[2]').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[4]/td[2]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH,
                                    '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div/div/div[4]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH,
                                        '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div/div/div[4]/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "The Liquor Shop",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_10.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 11 - "https://cellarbration.com.sg/" -

def age_verification_11():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="comp-k8on02nl"]/a')))
    driver.find_element(By.XPATH, '//*[@id="comp-k8on02nl"]/a').click()


def get_info_11(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[1]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[1]/div[2]/section/div/div/pre/p[4]').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/table/tbody/tr[4]/td[2]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[3]/div/div/div[2]/span[1]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH,'//*[@id="TPAMultiSection_jjnx2pgg"]/div/div/article/div[1]/section[2]/div[3]/div/div/div/span[1]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "gudsht",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_11.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 12 - "https://cellarbration.com.sg/" -

def age_verification_12():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button')))
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div/div/div[1]/button').click()


def get_info_12(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="sc-1bsd7ul-1 djlKtC"]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//span[@class="sc-13n2dsm-10 zrRPi quantity"]/span').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            try:
                volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/span[1]/span').text
            except:
                print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//div[@class="sc-scqi9x-2 itznBS"]/a[3]').text
    except:
        try:
            catagory = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]/a').text
        except:
            print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="sc-1bsd7ul-1 sc-13n2dsm-5 kxEbZl deQJPo"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "NUTC",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_12.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 13 - "https://cellarbration.com.sg/" -

def age_verification_13():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="preview_img"]/div[1]/section/div/div[2]/div[1]/button')))
    driver.find_element(By.XPATH, '//*[@id="preview_img"]/div[1]/section/div/div[2]/div[1]/button').click()


def get_info_13(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProductSection--product-template"]/div[4]/div[2]/div/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[3]/div/span[1]/span').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[1]/div[1]/a[4]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="ProductPrice"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Oak & Barrel",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_13.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 14 - "https://cellarbration.com.sg/" -

def get_info_14(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="akeeba-renderjoomla"]/div/div/div[1]/div[2]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[2]/td[2]/strong').text
        volume = int(volume)/10
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="akeeba-renderjoomla"]/div/div/div[1]/div[2]/div[2]/div[3]/div[1]/div').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "liquorbar",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_14.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 15 - "https://cellarbration.com.sg/" -

def age_verification_15():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wpforms-483-field_1_1"]')))
    driver.find_element(By.XPATH, '//*[@id="wpforms-483-field_1_1"]').click()
    driver.find_element(By.XPATH, '//*[@id="wpforms-submit-483"]').click()


def get_info_15(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="product-4216"]/div[2]/h1').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/p[2]/text()').text.replace("ml", "")
            # volume = int(volume)/10
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/p/ins/span/bdi').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div/div[2]/div[2]/p/ins/span/bdi/text()').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "thirstydonkey",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_15.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 16 - "https://cellarbration.com.sg/" -

def age_verification_16():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popmake-278"]/div[2]/p[4]/button')))
    driver.find_element(By.XPATH, '//*[@id="popmake-278"]/div[2]/p[4]/button').click()


def get_info_16(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/nav'))
        )
        productName2 = productName2.text
        productName_2 = productName2.split("/")
        productName2 = productName_2[-1]
        productName2 = productName2.replace("’", "")
    except:
        print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = productName_2[-2]
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/p[1]/ins/span/bdi').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div[2]/div[2]/p/span/bdi').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "tyliquor",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_16.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 17 - "https://cellarbration.com.sg/" -

def age_verification_17():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalWine"]/div/div/div/div[2]/div/div/div/form/button[1]')))
    driver.find_element(By.XPATH, '//*[@id="modalWine"]/div/div/div/div[2]/div/div/div/form/button[1]').click()


def get_info_17(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h2[@class="product__title"]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '//option[@selected="selected"]').text
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/span[1]/span').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//div[@class="sc-scqi9x-2 itznBS"]/a[3]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="product__price product__price--new money"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "winesnspirits",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_17.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 18 - "https://cellarbration.com.sg/" -

def get_info_18(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="product_header"]/div[2]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1].replace("ml", "")
        volume = int(volume)/10
    except:
        try:
            volume = productName2.split(" ")
            volume = volume[-1]
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[2]/div[2]/div[1]/div[2]/span/text()[2]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div[2]/div[2]/div[2]/form/span').text
        price = price.replace("S$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/span/span').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "Oaks Cellar",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_18.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 19 - "https://cellarbration.com.sg/" -

def age_verification_19():
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agp_row"]/div/div/div[4]/div/form[1]/input')))
    driver.find_element(By.XPATH, '//*[@id="agp_row"]/div/div/div[4]/div/form[1]/input').click()


def get_info_19(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ProductSection"]/div/div[2]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]').text
        except:
            print("Product Name not found for - ", url)

    try:
        volume = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/span').text
        volume = int(volume)/10
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-properties"]/tbody/tr[6]/td[2]/strong/a').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//*[@id="productPrice-product-template"]/span[1]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//*[@id="productPrice-product-template"]/span[1]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "boozemart",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_19.append(tempV)

#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------

# Functions for Site 20 - "https://cellarbration.com.sg/" -

# Functions for Site 20 - "https://cellarbration.com.sg/" -

def age_verification_20():
    pass


def get_info_20(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h1[@class="product-title mt-3"]'))
        )
        productName2 = productName2.text
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/span/span').text
        except:
            print("Product Name not found for - ", url)

    try:
        volumeObj = driver.find_elements(By.XPATH, '//tr')
        for i in volumeObj:
            if "Bottle volume ml" in i.find_element(By.XPATH, '//td[@class="product__properties__name"]').text:
                volume = i.find_element(By.XPATH, "//td[@class='product__properties__value']").text
                print("volume = ", volume)
    except:
        try:
            volume = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/span[1]/span').text
        except:
            print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/nav/div[1]/div/ol/li[3]/a/span').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="price price--selling price--discounted"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "paneco",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_20.append(tempV)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------

# Functions for Site 21 - "https://cellarbration.com.sg/" -

def age_verification_21():
    pass

def get_info_21(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume1 = ""
    catagory = ""
    price = ""

    try:
        productName2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="product-block product-block--header product-single__header small--hide"]/h1'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="ProductSection-template--14365883957351__main-4585757245543"]/div/div/div[1]/h1').text
            if productName2 == "":
                print("Product Name not found for - ", url)
        except:
            print("Product Name not found for - ", url)

    try:
        time.sleep(4)
        volume = driver.find_elements(By.XPATH, '//div[@class="collapsible-content__inner rte"][1]/p[1]')
        for i in volume:
            print(i)
        volume1 = volume[0].text
    except:
        print("Volume Not found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//span[@class="product__price"]/span[2]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "primeliquor",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume1,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_21.append(tempV)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------

# Functions for Site 22 - "https://cellarbration.com.sg/" -

def age_verification_22():
    # wait = WebDriverWait(driver, 30)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//md-checkbox[@type="type"]')))
    # time.sleep(5)
    # driver.find_element(By.XPATH, '//select/option[@value="1"]').click()
    # driver.find_element(By.XPATH, '//md-option[@id="select_option_18"]').click()
    # driver.find_element(By.XPATH, '//md-option[@id="select_option_75"]').click()
    # driver.find_element(By.XPATH, '//md-checkbox[@type="type"]').click()
    # driver.find_element(By.XPATH, '///button[@class="ageverify md-button md-ink-ripple"]').click()

    # drop1=Select(driver.find_element(By.XPATH, "//select[@name='userMonth']"))
    # drop1.select_by_value("1")

    # drop2=Select(driver.find_element(By.XPATH, "//select[@name='userDay']"))
    # drop2.select_by_value("1")

    driver.find_element(By.CSS_SELECTOR, '#select_16').click()
    driver.find_element(By.ID, 'select_option_4').click()

    driver.find_element(By.CSS_SELECTOR, '#select_49').click()
    driver.find_element(By.ID, 'select_option_18').click()

    driver.find_element(By.CSS_SELECTOR, '#select_51').click()
    driver.find_element(By.ID, 'select_option_75').click()

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ageverify md-button md-ink-ripple"]')))

    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@class="ageverify md-button md-ink-ripple"]').click()

def get_info_22(url):
    try:
        driver.get(url)
    except:
        print("Url Invalid")

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""

    try:
        time.sleep(5)
        productName2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="prddetailtitle ng-binding"]'))
        )
        productName2 = productName2.text
        productName2 = productName2.replace("’", "")
    except:
        try:
            productName2 = driver.find_element(By.XPATH, '//*[@id="ProductSection-template--14365883957351__main-4585757245543"]/div/div/div[1]/h1').text
            if productName2 == "":
                print("Product Name not found for - ", url)
        except:
            print("Product Name not found for - ", url)

    try:
        volume = productName2.split(" ")
        volume = volume[-1]
    except:
        try:
            volume = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div/div[1]/div/div/div/p[1]/text()[2]').text
        except:
            try:
                volume = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div/div[1]/div/div/div/p[1]/strong[1]').text
            except:
                print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//a[@class="ng-binding ng-scope"]').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH, '//div[@class="prddetailpricedicnt ng-binding ng-scope"]').text
        price = price.replace("$", "")
    except:
        try:
            price = driver.find_element(By.XPATH, '//span[@class="price price--selling"]').text
            price = price.replace("$", "")
        except:
            print("Price not found for - ", url)

    tempV = {
        "Site": "alcoholdelivery",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Price": price,
        "Product Link": url}

    finalData_22.append(tempV)

#-------------------------------------------------------------------------------------


# All Driver Codes -


# -------------------------------------------------------------------------------------

# Driver Code 1 -

# driver = webdriver.Chrome(ChromeDriverManager().install())  # For IDE (Uncomment in IDE)

site_name = ["https://cellarbration.com.sg/", "https://alcohaul.sg/", "https://www.alcoholporter.com/", "https://www.bnb.com.sg/", "https://chuansenghuat.com.sg/", "https://coldstorage.com.sg/", "https://shop.cornerstonewines.com/", "https://getit.changirecommends.com/", "https://giant.sg/", "https://www.theliquorshop.com.sg/", "https://www.gudsht.org/", "https://www.fairprice.com.sg/", "https://oakandbarrel.com.sg/", "https://www.liquorbar.sg/", "https://thirstydonkey.sg/", "https://www.tyliquor.sg/", "https://www.winesnspirits.sg/", "https://www.oaks.com.sg/", "https://boozemart.sg/","https://www.paneco.com.sg/","https://www.primeliquor.sg/","https://www.alcoholdelivery.com.sg/"]

for sn in site_name:
    driver.get(sn)
    print(">> ", driver.title)

    if sn == "https://cellarbration.com.sg/":
        try:
            age_verification_1()
        except:
            print("Age verification failed")
        for lnk2 in uniqueLnks_1:
            get_info_1(lnk2)
            print("Final Data :- ", finalData_1[-1])
            print("No of Product Info. :- ", len(finalData_1))
            print(finalData_1[-1])
        clean_data_1 = [i for n, i in enumerate(finalData_1) if i not in finalData_1[n + 1:]]
        clean_data_1 = [i for i in clean_data_1 if not (i['Product Name'] == "")]

    elif sn == "https://alcohaul.sg/":
        try:
            age_verification_2()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_2:
            get_info_2(lnk2)
            print("Final Data :- ", finalData_2[-1])
            print("No of Product Info. :- ", len(finalData_2))
            print(finalData_2[-1])
        clean_data_2 = [i for n, i in enumerate(finalData_2) if i not in finalData_2[n + 1:]]
        clean_data_2 = [i for i in clean_data_2 if not (i['Product Name'] == "")]

    elif sn == "https://www.alcoholporter.com/":
        try:
            age_verification_3()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_3:
            get_info_3(lnk2)
            print("Final Data :- ", finalData_3[-1])
            print("No of Product Info. :- ", len(finalData_3))
            print(finalData_3[-1])
        clean_data_3 = [i for n, i in enumerate(finalData_3) if i not in finalData_3[n + 1:]]
        clean_data_3 = [i for i in clean_data_3 if not (i['Product Name'] == "")]

    elif sn == "https://www.bnb.com.sg/":
        try:
            age_verification_4()
        except:
            print("Age verification  failed")
        for lnk2 in uniqueLnks_4:
            get_info_4(lnk2)
            print("Final Data :- ", finalData_4[-1])
            print("No of Product Info. :- ", len(finalData_4))
            print(finalData_4[-1])
        clean_data_4 = [i for n, i in enumerate(finalData_4) if i not in finalData_4[n + 1:]]
        clean_data_4 = [i for i in clean_data_4 if not (i['Product Name'] == "")]

    elif sn == "https://chuansenghuat.com.sg/":
        for lnk2 in uniqueLnks_5:
            get_info_5(lnk2)
            print("Final Data :- ", finalData_5[-1])
            print("No of Product Info. :- ", len(finalData_5))
            print(finalData_5[-1])
        clean_data_5 = [i for n, i in enumerate(finalData_5) if i not in finalData_5[n + 1:]]
        clean_data_5 = [i for i in clean_data_5 if not (i['Product Name'] == "")]

    elif sn == "https://coldstorage.com.sg/":
        for lnk2 in uniqueLnks_6:
            r = requests.get(lnk2)
            stat_code = r.status_code
            if stat_code == 200:
                get_info_6(lnk2)
                print("Final Data :- ", finalData_6[-1])
                print("No of Product Info. :- ", len(finalData_6))
                print(finalData_6[-1])
            else:
                time.sleep(30)
        clean_data_6 = [i for n, i in enumerate(finalData_6) if i not in finalData_6[n + 1:]]
        clean_data_6 = [i for i in clean_data_6 if not (i['Product Name'] == "")]

    elif sn == "https://shop.cornerstonewines.com/":
        for lnk2 in uniqueLnks_7:
            get_info_7(lnk2)
            print("Final Data :- ", finalData_7[-1])
            print("No of Product Info. :- ", len(finalData_7))
            print(finalData_7[-1])
        clean_data_7 = [i for n, i in enumerate(finalData_7) if i not in finalData_7[n + 1:]]
        clean_data_7 = [i for i in clean_data_7 if not (i['Product Name'] == "")]

    elif sn == "https://getit.changirecommends.com/":
        for lnk2 in uniqueLnks_8:
            get_info_8(lnk2)
            print("Final Data :- ", finalData_8[-1])
            print("No of Product Info. :- ", len(finalData_8))
            print(finalData_8[-1])
        clean_data_8 = [i for n, i in enumerate(finalData_8) if i not in finalData_8[n + 1:]]
        clean_data_8 = [i for i in clean_data_8 if not (i['Product Name'] == "")]
    elif sn == "https://giant.sg/":
        for lnk2 in uniqueLnks_9:
            get_info_9(lnk2)
            print("Final Data :- ", finalData_9[-1])
            print("No of Product Info. :- ", len(finalData_9))
            print(finalData_9[-1])
        clean_data_9 = [i for n, i in enumerate(finalData_9) if i not in finalData_9[n + 1:]]
        clean_data_9 = [i for i in clean_data_9 if not (i['Product Name'] == "")]

    elif sn == "https://www.theliquorshop.com.sg/":
        for lnk2 in uniqueLnks_10:
            get_info_10(lnk2)
            print("Final Data :- ", finalData_10[-1])
            print("No of Product Info. :- ", len(finalData_10))
            print(finalData_10[-1])
        clean_data_10 = [i for n, i in enumerate(finalData_10) if i not in finalData_10[n + 1:]]
        clean_data_10 = [i for i in clean_data_10 if not (i['Product Name'] == "")]

    elif sn == "https://www.gudsht.org/":
        for lnk2 in uniqueLnks_11:
            get_info_11(lnk2)
            print("Final Data :- ", finalData_11[-1])
            print("No of Product Info. :- ", len(finalData_11))
            print(finalData_11[-1])
        clean_data_11 = [i for n, i in enumerate(finalData_11) if i not in finalData_11[n + 1:]]
        clean_data_11 = [i for i in clean_data_11 if not (i['Product Name'] == "")]

    elif sn == "https://www.fairprice.com.sg/":
        for lnk2 in uniqueLnks_12:
            get_info_12(lnk2)
            print("Final Data :- ", finalData_12[-1])
            print("No of Product Info. :- ", len(finalData_12))
            print(finalData_12[-1])
        clean_data_12 = [i for n, i in enumerate(finalData_12) if i not in finalData_12[n + 1:]]
        clean_data_12 = [i for i in clean_data_12 if not (i['Product Name'] == "")]

    elif sn == "https://oakandbarrel.com.sg/":
        try:
            age_verification_13()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_13:
            get_info_13(lnk2)
            print("Final Data :- ", finalData_13[-1])
            print("No of Product Info. :- ", len(finalData_13))
            print(finalData_13[-1])
        clean_data_13 = [i for n, i in enumerate(finalData_13) if i not in finalData_13[n + 1:]]
        clean_data_13 = [i for i in clean_data_13 if not (i['Product Name'] == "")]

    elif sn == "https://www.liquorbar.sg/":
        for lnk2 in uniqueLnks_14:
            get_info_14(lnk2)
            print("Final Data :- ", finalData_14[-1])
            print("No of Product Info. :- ", len(finalData_14))
            print(finalData_14[-1])
        clean_data_14 = [i for n, i in enumerate(finalData_14) if i not in finalData_14[n + 1:]]
        clean_data_14 = [i for i in clean_data_14 if not (i['Product Name'] == "")]

    elif sn == "https://thirstydonkey.sg/":
        try:
            age_verification_15()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_15:
            get_info_15(lnk2)
            print("Final Data :- ", finalData_15[-1])
            print("No of Product Info. :- ", len(finalData_15))
            print(finalData_15[-1])
        clean_data_15 = [i for n, i in enumerate(finalData_15) if i not in finalData_15[n + 1:]]
        clean_data_15 = [i for i in clean_data_15 if not (i['Product Name'] == "")]

    elif sn == "https://www.tyliquor.sg/":
        try:
            age_verification_16()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_16:
            get_info_16(lnk2)
            print("Final Data :- ", finalData_16[-1])
            print("No of Product Info. :- ", len(finalData_16))
            print(finalData_16[-1])
        clean_data_16 = [i for n, i in enumerate(finalData_16) if i not in finalData_16[n + 1:]]
        clean_data_16 = [i for i in clean_data_16 if not (i['Product Name'] == "")]

    elif sn == "https://www.winesnspirits.sg/":
        try:
            age_verification_17()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_17:
            get_info_17(lnk2)
            print("Final Data :- ", finalData_17[-1])
            print("No of Product Info. :- ", len(finalData_17))
            print(finalData_17[-1])
        clean_data_17 = [i for n, i in enumerate(finalData_17) if i not in finalData_17[n + 1:]]
        clean_data_17 = [i for i in clean_data_17 if not (i['Product Name'] == "")]

    elif sn == "https://www.oaks.com.sg/":
        for lnk2 in uniqueLnks_18:
            get_info_18(lnk2)
            print("Final Data :- ", finalData_18[-1])
            print("No of Product Info. :- ", len(finalData_18))
            print(finalData_18[-1])
        clean_data_18 = [i for n, i in enumerate(finalData_18) if i not in finalData_18[n + 1:]]
        clean_data_18 = [i for i in clean_data_18 if not (i['Product Name'] == "")]

    elif sn == "https://boozemart.sg/":
        try:
            age_verification_19()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_19:
            get_info_19(lnk2)
            print("Final Data :- ", finalData_19[-1])
            print("No of Product Info. :- ", len(finalData_19))
            print(finalData_19[-1])
        clean_data_19 = [i for n, i in enumerate(finalData_19) if i not in finalData_19[n + 1:]]
        clean_data_19 = [i for i in clean_data_19 if not (i['Product Name'] == "")]

    elif sn == "https://www.paneco.com.sg/":
        try:
            age_verification_20()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_20:
            get_info_20(lnk2)
            print("Final Data :- ", finalData_20[-1])
            print("No of Product Info. :- ", len(finalData_20))
            print(finalData_20[-1])
        clean_data_20 = [i for n, i in enumerate(finalData_20) if i not in finalData_20[n + 1:]]
        clean_data_20 = [i for i in clean_data_20 if not (i['Product Name'] == "")]

    elif sn == "https://www.primeliquor.sg/":
        try:
            age_verification_22()
        except:
            print("Age verification failed !")
        for lnk2 in uniqueLnks_21:
            get_info_21(lnk2)
            print("Final Data :- ", finalData_21[-1])
            print("No of Product Info. :- ", len(finalData_21))
            print(finalData_21[-1])
        clean_data_21 = [i for n, i in enumerate(finalData_21) if i not in finalData_21[n + 1:]]
        clean_data_21 = [i for i in clean_data_21 if not (i['Product Name'] == "")]

    elif sn == "https://www.alcoholdelivery.com.sg/":
        try:
            age_verification_22()
        except Exception as e:
            print("Age verification failed !", e)
        for lnk2 in uniqueLnks_22:
            get_info_22(lnk2)
            print("Final Data :- ", finalData_22[-1])
            print("No of Product Info. :- ", len(finalData_22))
            print(finalData_22[-1])
        clean_data_22 = [i for n, i in enumerate(finalData_22) if i not in finalData_22[n + 1:]]
        clean_data_22 = [i for i in clean_data_22 if not (i['Product Name'] == "")]
    else:
        driver.close()

driver.close()

# Final Processing -

clean_data = [*clean_data_1, *clean_data_2, *clean_data_3, *clean_data_4, *clean_data_5, *clean_data_6, *clean_data_7, *clean_data_8, *clean_data_9, *clean_data_10, *clean_data_11, *clean_data_12, *clean_data_13, *clean_data_14, *clean_data_15, *clean_data_16, *clean_data_17, *clean_data_18, *clean_data_19, *clean_data_20, *clean_data_21, *clean_data_22]
print(clean_data)
print(len(clean_data))

# Data Saving -

# Saving the Data to Excel Sheet -

df = pd.DataFrame.from_dict(clean_data)
print(df)
df.to_excel('finalData.xlsx', index=False)

# To Save Data in JSON file -
import json


def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data(title):
    with open(title, encoding="utf-8") as f:
        return json.load(f)


save_data("finalData.json", clean_data)

# ........................................................................................

# To Store Scraped Data in MYSQL Database (Remote Database) -
try:
    engine = create_engine("mysql+pymysql://dev:devAverps3985$$@128.199.122.126/uddipan?charset=utf8mb4")
    df = pd.read_json("finalData.json")
    df.to_sql("Product_prices", con=engine, if_exists="replace", index=False)
    print("Data updated in Database...")
except Exception as e:
    print(">> Cannot Connect to Database", e)

# ........................................................................................


print("--------------------------------------------")

logFile = open("scrapperLogs.txt", "a")

ct1 = datetime.datetime.now()

print("Start Time :-", ct)
print("End Time :-", ct1)

ct = str(ct)
ct1 = str(ct1)
logFile.write(str("Start Time = " + str(ct)))
logFile.write(str("Stop Time = " + str(ct1)))

logFile.close()

print("--------------------------------------------")


