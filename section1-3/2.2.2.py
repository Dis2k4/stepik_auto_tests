from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    sum=0
    input1 = browser.find_element(By.ID, "num1")
    input2 = browser.find_element(By.ID, "num2")
    sum=int(input1.text)+int(input2.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum)) # ищем элемент с текстом "Python"
    Button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    Button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла