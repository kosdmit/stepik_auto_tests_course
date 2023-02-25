import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



LINK = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(LINK)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_value.text

y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, '#answer')
try:
    input.send_keys(y)
except selenium.common.exceptions.ElementClickInterceptedException:
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(20)

browser.quit()

