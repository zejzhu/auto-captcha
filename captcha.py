from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import ChromeDriverManager
from dotenv import load_dotenv
import pytesseract
from PIL import Image
import tempfile
import requests
import os
'''
infinitely sends captcha using ocr
'''
load_dotenv()
'''
Replace these variables with the correct path to tessract, captcha website url, captcha locator, and input locator
'''
url = os.getenv("URL")
captcha_identifier = os.getenv("CAPTCHA_ID")
input_identifier = os.getenv("INPUT_ID")
tesseract_path = os.getenv("TESSERACT_PATH")



# selenium time
service = Service(ChromeDriverManager().install)
driver = webdriver.Chrome(service=service)

driver.get(url)
captcha_element = driver.find_element_by_xpath(captcha_identifier)
input_element = driver.find_element_by_xpath()



