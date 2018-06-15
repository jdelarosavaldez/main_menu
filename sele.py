from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys

import time
import requests


# driver = webdriver.Chrome('chromedriver')
driver = webdriver.Firefox()
driver.get("")
time.sleep(5)

# menu_items = driver.find_element_by_id('menu-main-menu')
# items = menu_items.find_elements_by_class_name('menu-item')
items = self.driver.find_elements_by_css_selector('#menu-main-menu .menu-item.nav-servicios')
# print(items, len(items))
for i in range(0,len(items)):
    # if 'menu-item-object-servicio' in items[i].get_attribute('class'):
    print(items[i].text)






driver.quit()

# for i in range(0, len(items)):
    # if 'menu-item-object-page' in items[i].get_attribute('class'):
        # element = items[i].find_element_by_tag_name('a')
        # print(element.text)


        # try:
        #     old_url = driver.current_url
        #     main_window = driver.window_handles[0]
        #     print(main_window)

        #     actions = AC(driver)
        #     # actions.key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
        #     actions.key_down(Keys.SHIFT)
        #     time.sleep(0.5)
        #     actions.click(element)
        #     actions.key_up(Keys.SHIFT)
        #     actions.perform()
        #     time.sleep(5)

        #     multiple_window = driver.window_handles
        #     # print(multiple_window)
        #     errors = 0

        #     for each_window in multiple_window[:0:-1]:
        #         print(each_window)
        #         driver.switch_to_window(each_window)
        #         time.sleep(10)
        #         # new_url, page_is_404 = verify_and_close(driver)
        #         new_url = driver.current_url
        #         print(new_url)
                
        #         # if driver.find_element_by_class_name('error404'):
        #         #     page_is_404 = True
        #         # else:
        #         #     page_is_404 = False
        #         # print('404=',page_is_404)
        #         driver.close()
        #         driver.switch_to_window(main_window)

        #         status = old_url != new_url #and page_is_404 is False
        #         if not status:
        #             errors += 1
        #             print(errors)

        #         print(status)

        # except:
        #     print('jodia except',False)



# def is_current_page_404(driver):
#     try:
#         exists_fourofour = driver.find_element_by_class_name('error404')
#         return True
#     except:
#         return False


# def switch_to_window(driver, window_index=0, by_index=True, handle=None):
#     if not by_index:
#         return driver.switch_to_window(handle)
#     return driver.switch_to_window(driver.window_handles[window_index])


# def verify_and_close(driver):
#     new_url = driver.current_url
#     page_is_404 = is_current_page_404(driver)
#     driver.close()
#     return new_url, page_is_404

    # driver.find_element_by_partial_link_text(items[i].text).click()
    # try:
    #     element = driver.find_element_by_partial_link_text(items[i].text)
    #     handles = driver.window_handles
    #     ActionChains(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
    #     time.sleep(2)
    #     driver.switch_to.window(handles[1])
    #     time.sleep(2)
    #     print(driver.current_url)
    #     driver.close()
    #     driver.switch_to.window(handles[0])
    # except:
    #     print(items[i].text)

    # elif 'nav-servicios' in items[i].get_attribute('class') and items[i].get_attribute('id') == 'menu-item-209':
    #     element = items[i].find_element_by_tag_name('a').text
    #     no_link = element.get_attribute('href')
    #     if no_link == '#':
    #         print(element.text)

    # window_after = driver.window_handles
    # driver.switch_to_window(window_after)
    # print(window_after)
    # time.sleep(2)
    # print(driver.current_url)
    # driver.close()
    # driver.switch_to_window(window_before)
    # main_window = driver.current_window_handle
    # element.send_keys(Keys.COMMAND + Keys.RETURN)
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.NUMPAD2)
    # driver.switch_to_window(main_window)
    # time.sleep(10)
    # print(driver.current_url)
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    # # driver.switch_to_window(main_window)
    # print(driver.current_url)

# menu-item-209 > a
# //*[@id="menu-item-229"]/a



