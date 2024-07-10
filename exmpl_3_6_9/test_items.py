import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    button=browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, 'Button not found!!!'