from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

LINK = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(LINK)

x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
x = x_element.get_attribute('valuex')
y = calc(x)

text_input = browser.find_element(By.CSS_SELECTOR, '#answer')
text_input.send_keys(y)

check_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
check_box.click()

radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radio.click()

submit = browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
submit.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()