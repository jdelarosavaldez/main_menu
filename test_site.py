import unittest
import time
import page
import variable as v

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys


class mainMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # cls.driver = webdriver.Chrome('chromedriver')
        cls.driver.get(v.url[0])
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
        self.assertEqual(menu_elements, v.elements, 'The Menu Elements missing and/or has incorrect Elements')

    def test_menu_elements_links(self):
        """ Homepage - Menu Elements Links, Verifying The Elements/items links are complete or corret"""
        elements_links = []
        items = self.main_page.get_main_menu_elements()
        for i in range(0, len(items)):
            if v.html_class[0] in items[i].get_attribute('class'):  # menu-item-object-page
                elements_links.append(items[i].find_element_by_tag_name('a').get_attribute('href'))
        self.assertEqual(elements_links, v.links, 'The Menu Links missing and/or has incorrect Links')

    def test_menu_elements_redirect(self):
        """ Homepage - Menu Element, Verifying The Redirection and if is Clickable"""
        driver = self.driver
        items = self.main_page.get_main_menu_elements()
        for i in range(0, len(items)):
            if v.html_class[0] in items[i].get_attribute('class'):
                element = items[i].find_element_by_tag_name('a')

                try:
                    old_url = self.driver.current_url
                    main_window = self.driver.window_handles[0]
                    # print(main_window)

                    actions = AC(self.driver)
                    # actions.key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
                    actions.key_down(Keys.SHIFT)
                    time.sleep(0.5)
                    actions.click(element)
                    actions.key_up(Keys.SHIFT)
                    actions.perform()
                    time.sleep(5)

                    multiple_window = self.driver.window_handles
                    for each_window in multiple_window[:0:-1]:
                        self.driver.switch_to_window(each_window)
                        time.sleep(5)
                        new_url = self.driver.current_url

                        try:
                            exists_404 = driver.find_element_by_class_name('error404')
                            page_is_404 = True
                        except:
                            page_is_404 = False

                        self.driver.close()
                        self.driver.switch_to_window(main_window)

                        status = old_url != new_url and page_is_404 is False
                        self.assertTrue(status, "Not Clickable or Page 404: {}".format(element.get_attribute('href')))

                except:
                    print(element.text)


    def test_sub_menu_objects(self):
        """ Homepage - Sub Menu Elements, Verifying The Sub Elements/items with custom are complete or corret"""
        items = self.main_page.get_main_menu_elements()
        for i in range(0,len(items)):
            if 'menu-item-object-servicio' in items[i].get_attribute('class'):
                self.assertTrue(items[i].text in v.sub_elements, "The {} is not in the SubMenu/Service".format(items[i].text))

            

    def test_sub_menu_objects_link(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
