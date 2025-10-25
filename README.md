# Infinitely send CAPTCHA answers using OCR.
This script uses Selenium and Tesseract OCR to determine captcha answers and continuously input them to the site's answer form.

You simply need to edit the variables for site url, web element locators, and the path to your tesseract executable (if tesseract is not in your PATH)

# Dependencies
- selenium
- webdriver_manager (my preference)
- dotenv
- pytesseract
- Pillow
