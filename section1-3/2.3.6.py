from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.TAG_NAME,"button")
    button1.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    y=0
    input1 = browser.find_element(By.ID, "input_value")
    y = calc(input1.text)
    input2 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input2.send_keys(str(y))
    button1 = browser.find_element(By.TAG_NAME,"button")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла