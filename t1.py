import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test6(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("a[href='http://localhost/litecart/admin/?app=appearance&doc=template']").click()
    driver.find_element_by_tag_name("h1")
    lst=[]
    lst1=[]
    lst=driver.find_elements_by_id("app-")
    for i in range(len(lst)):
        lst1=driver.find_elements_by_id("app-")
        print(i,' ',len(lst1))
    WebDriverWait(driver, 20).until(EC.title_is("Template | My Store"))