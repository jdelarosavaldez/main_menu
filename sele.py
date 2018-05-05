from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import request


driver = webdriver.Chrome('chromedriver')
# driver = webdriver.Firefox()
driver.get("https://www.gbh.com.do/")
time.sleep(5)

menu_items = driver.find_element_by_id('menu-main-menu')
items = menu_items.find_elements_by_class_name('menu-item')
# print(items, len(items))
# print(items[1].get_attribute('class'), items[1].text)
for i in range(0,len(items)):
    if 'asdfasdfasdf' in items[i].get_attribute('class'): #menu-item-object-page
        # driver.find_element_by_partial_link_text(items[i].text).click()
        try:
            element = driver.find_element_by_partial_link_text(items[i].text)
            handles = driver.window_handles
            ActionChains(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
            time.sleep(2)
            driver.switch_to.window(handles[1])
            time.sleep(2)
            print(driver.current_url)
            driver.close()
            driver.switch_to.window(handles[0])
        except:
            print(items[i].text)

    elif 'nav-servicios' in items[i].get_attribute('class') and items[i].get_attribute('id') == 'menu-item-209':
        element = items[i].find_element_by_tag_name('a').text
        no_link = element.get_attribute('href')
        if no_link == '#':
            print(element.text)
            

# menu-item-209 > a
# //*[@id="menu-item-229"]/a



driver.quit()
