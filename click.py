from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    browser.implicitly_wait(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id = 'price"), "100"))

    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '[id = "input_value"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text

    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')


    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, '[id = "solve"]')
    button2.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()