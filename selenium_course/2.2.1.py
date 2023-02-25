import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

LINK = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(LINK)

num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
num1 = int(num1.text)
num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
num2 = int(num2.text)
sum = num1 + num2


select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
select.select_by_visible_text(str(sum))

submit = browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
submit.click()

time.sleep(30)

browser.quit()





