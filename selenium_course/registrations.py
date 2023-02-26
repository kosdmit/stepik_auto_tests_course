import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("kosdmitos@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
        input4.send_keys("927")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("kosdmitos@mail.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
        input4.send_keys("927")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)