import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_in_cart(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-a1dd-to-basket"), 'Button is absent'