from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_abs1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("First")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input2.send_keys("Second")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input3.send_keys("Third")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    time.sleep(10)
    browser.quit()
    assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute value of a number"

def test_abs2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("First")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    input2.send_keys("Second")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    input3.send_keys("Third")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    time.sleep(10)
    browser.quit()
    assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")