import unittest
import time
import page
from selenium import webdriver

objetos = ['INICIO', 'PORTAFOLIO','CONÓCENOS', 'EMPLEOS','BLOG']

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

    def test_menu_objects(self):
        """ Homepage - Menu Objects, Verifying The Elements/items without custom are correct"""
        menu_objects = []
        items = self.main_page.get_main_menu_elements()
        for i in range(0, len(items)):
            if 'menu-item-object-page' in items[i].get_attribute('class'):  # menu-item-object-page
                menu_objects.append(items[i].text)
        self.assertEqual(menu_objects, objetos,'The Menu Objects are corrects')


    def test_menu_objects_link(self):
        pass

    def test_menu_objects_redirect(self):
        pass

    def test_sub_menu_objects(self):
        pass

    def test_sub_menu_objects(self):
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
