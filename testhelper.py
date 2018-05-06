import time
import requests
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys


def click_and_open_tab(element, driver, menu_elements, handles):
    AC(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
    time.sleep(2)
    driver.switch_to.window(handles[1])
    time.sleep(2)
    # r = requests.get(driver.current_url)
    # menu_elements.append(driver.current_url, r.status_code)
    driver.close()
    driver.switch_to.window(handles[0])
    return menu_elements
