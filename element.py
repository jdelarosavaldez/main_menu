from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    name = 'BaseElement'
    time_out = 10
    parent = None

    def __init__(self, driver=None, parent=None):
        self.driver = driver
        if parent:
            self.parent = parent