from selenium import webdriver
from selenium.webdriver.common.by import By
#https://www.demoblaze.com/
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser


def test_open_s6(browser):
    browser.get('https://www.demoblaze.com/index.html')
    galaxy_s6 = browser.find_element(By.LINK_TEXT.find('Samsung galaxy s6')
    galaxy_s6.click()
