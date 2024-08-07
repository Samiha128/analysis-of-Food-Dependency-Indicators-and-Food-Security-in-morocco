import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import logging


logging.basicConfig(level=logging.CRITICAL)


options = Options()
options.headless = True 

try:
   
    driver = webdriver.Firefox(options=options)

   
    driver.get('https://data.gov.ma/data/fr/dataset/cheptel-2010-2021')

   
    wait = WebDriverWait(driver, 10)
    explorer_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.btn-primary.dropdown-toggle')))
    explorer_button.click()

    
    download_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.resource-url-analytics')))
    download_link.click()

   
    time.sleep(10)

finally:
   
    driver.quit()
