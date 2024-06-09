import time
import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
def test_guest_can_go_to_login_page(browser):
    site_link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, site_link)
    page.open()
    page.go_to_login_page()
    time.sleep(4)



