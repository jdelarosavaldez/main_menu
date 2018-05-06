import unittest
import time
import page
import testhelper
import requests

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

elements = ['INICIO', 'PORTAFOLIO', 'CONÓCENOS', 'EMPLEOS', 'BLOG']
links = [
    'http://gbh.com.do/',
    'http://gbh.com.do/portafolio/',
    'http://gbh.com.do/soluciones-gbh/',
    'http://gbh.com.do/empleos/',
    'http://gbh.com.do/noticias-de-tecnologia/']


class mainMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Chrome('chromedriver')
        cls.driver.get("http://www.gbh.com.do")
        cls.main_page = page.HomePage(cls.driver)
        time.sleep(5)
        # print(cls.driver.title)

    def test_verify_title_site(self):
        """ Homepage - Title, Verifying The Title if correct """
        title = self.main_page.is_title_matches()
        self.assertTrue(title, "Title doesn't Match")

    def test_logo_link(self):
        """ Homepage - Logo, Test the logo link if not redict to 404 page """
        images_link = self.main_page.get_logo()
        images_link.click()
        is_404 = 'error404'
        self.assertTrue(is_404 not in self.driver.page_source, "Logo Link getting 404 page")

    def test_menu_elements(self):
        """ Homepage - Menu Elements, Verifying The Elements/items without custom are complete or corret"""
        menu_elements = []
        items = self.main_page.get_main_menu_elements()
        for i in range(0, len(items)):
            if 'menu-item-object-page' in items[i].get_attribute('class'):  # menu-item-object-page
                menu_elements.append(items[i].text)
        self.assertEqual(menu_elements, elements, 'The Menu Elements missing and/or has incorrect Elements')

    def test_menu_elements_links(self):
        """ Homepage - Menu Elements Links, Verifying The Elements/items links are complete or corret"""
        elements_links = []
        items = self.main_page.get_main_menu_elements()
        for i in range(0, len(items)):
            if 'menu-item-object-page' in items[i].get_attribute('class'):  # menu-item-object-page
                elements_links.append(items[i].find_element_by_tag_name('a').get_attribute('href'))
        self.assertEqual(elements_links, links, 'The Menu Links missing and/or has incorrect Links')

    def test_menu_elements_redirect(self):
        """ Homepage - Menu Element, Verifying The Redirection and if is Clickable"""
        menu_elements = []
        driver = self.main_page
        items = driver.get_main_menu_elements()
        for i in range(0, len(items)):
            if 'menu-item-object-page' in items[i].get_attribute('class'):  # menu-item-object-page
                try:
                    element = driver.find_element_by_partial_link_text(items[i].text)
                    handles = driver.window_handles
                    # menu_elements = testhelper.click_and_open_tab(element, dr, menu_elements, handles,)
                    AC(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
                    time.sleep(2)
                    driver.switch_to.window(handles[1])
                    time.sleep(2)
                    # r = requests.get(driver.current_url)
                    # menu_elements.append(driver.current_url, r.status_code)
                    driver.close()
                    driver.switch_to.window(handles[0])
                except:
                    menu_elements.append("can't click on {}".format(items[i].text))
        print(menu_elements)
        self.assertIn('400', menu_elements, "Can't Click and open other tab in some element")

    def test_sub_menu_objects(self):
        pass

    def test_sub_menu_objects_link(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    # def find_element(self, by, value):
    #     try:
    #         return self.driver.find_element(by, value)
    #     except NoSuchElementException:
    #         return None


if __name__ == "__main__":
    unittest.main(verbosity=2)
