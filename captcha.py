from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import pytesseract
from PIL import Image
import tempfile
import os
from time import sleep


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


# selenium time (installs chrome webdriver using webdriver_manager)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)
sleep(2)

captcha_counter = 0
while True:
    # screenshot captcha image and save to a temporary file
    # (src is constantly refreshing so you need to screenshot)
    captcha_element = driver.find_element(By.XPATH, captcha_identifier)

    with tempfile.NamedTemporaryFile(delete=True, suffix='.png') as temp_img:
        captcha_element.screenshot(temp_img.name)

        # use OCR to get captcha answer
        image = Image.open(temp_img.name)
        answer = pytesseract.image_to_string(image)

    # type the answer into the input form
    input_element = driver.find_element(By.XPATH, input_identifier)
    input_element.send_keys(answer)
    input_element.send_keys(Keys.ENTER)

    captcha_counter += 1
    print(captcha_counter, end=', ')
    sleep(0.5)




