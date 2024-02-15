from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код

    x = browser.find_element(By.CSS_SELECTOR, '[id = "num1"]')
    x = x.text
    y = browser.find_element(By.CSS_SELECTOR, '[id = "num2"]')
    y = y.text

    total = str(int(x)+int(y))

    select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
    select = select.select_by_value(total)

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