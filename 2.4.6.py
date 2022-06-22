from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    pricelabel = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button1 = browser.find_element(By.TAG_NAME,"button")
    button1.click()
    input1 = browser.find_element(By.ID, "input_value")
    y = calc(input1.text)
    input2 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input2.send_keys(str(y))
    button2 = browser.find_element(By.ID,"solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
