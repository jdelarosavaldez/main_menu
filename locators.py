from selenium.webdriver.common.by import By


class HomePageLocators(object):

    LOGO_SITE      = (By.CLASS_NAME, 'branding')
    MAIN_MENU      = (By.ID, 'menu-main-menu')
    MAIN_MENU_ITEMS = (By.CLASS_NAME,'menu-item' )
