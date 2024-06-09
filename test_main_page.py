import time

import pytest
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    site_link = "http://selenium1py.pythonanywhere.com/"
    browser.get(site_link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(3)

