import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, language):
    link = f"https://stepik.org/lesson/{language}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    textcheck=browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert textcheck=="Correct!", f"{language} incorrect"