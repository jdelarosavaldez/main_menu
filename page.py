from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from element import BasePageElement
from locators import HomePageLocators


class BasePage(object):
    url = ''

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def is_title_matches(self):
        return "soluciones gbh" in self.driver.title.lower()

    def get_logo(self):
        logo_site = self.driver.find_element(*HomePageLocators.LOGO_SITE)
        return logo_site

    def get_main_menu_elements(self):
        main_menu = self.driver.find_element(*HomePageLocators.MAIN_MENU)
        items = main_menu.find_elements(*HomePageLocators.MAIN_MENU_ITEMS)
        return items
