import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

LINK = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(LINK)

x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_value.text

y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, '#answer')
try:
    input.send_keys(y)
except selenium.common.exceptions.ElementClickInterceptedException:
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
try:
    checkbox.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
try:
    radio.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()



button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(20)

browser.quit()