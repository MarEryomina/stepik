from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код

    input1 = browser.find_element(By.CSS_SELECTOR, 'input')
    input1.send_keys('ok')

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name ="lastname"]')
    input1.send_keys('ok')

    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name ="email"]')
    input2.send_keys('ok')

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, 'ok.txt')
    file = browser.find_element(By.CSS_SELECTOR, '[id = "file"]')
    file.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()