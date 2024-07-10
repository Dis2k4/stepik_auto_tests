from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.ID, "treasure")
    y = calc(input1.get_attribute("valuex"))
    input2 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input2.send_keys(str(y))
    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option2.click()
    Button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    Button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла