import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import logging

logging.basicConfig(level=logging.CRITICAL)

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    
    driver.get('https://www.data.gov.ma/data/fr/dataset/mer-en-chiffre-2020-production-halieutique')

   
    wait = WebDriverWait(driver, 10)
    explorer_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.btn-primary.dropdown-toggle')))
    explorer_button.click()

   
    download_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.resource-url-analytics')))
    download_link.click()

    
    time.sleep(10)  
finally:
    driver.quit()
