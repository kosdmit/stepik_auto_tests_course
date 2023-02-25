from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import os

LINK = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(LINK)

input_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
input_name.send_keys('Vanya')

input_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input_lastname.send_keys('Ivanov')

input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
input_email.send_keys('Ivanov@vanya.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '../README.md')

uploader = browser.find_element(By.CSS_SELECTOR, '#file')
uploader.send_keys(file_path)

submit = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
submit.click()

time.sleep(20)

browser.quit()