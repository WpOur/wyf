from selenium import  webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.suning.com/")

driver.find_element_by_name("utf-8_homepagev8_126605238628_word01").click()

a=driver.window_handles
driver.switch_to.window(a[-1])

driver.find_element_by_xpath("/html/body/div[6]/div[2]/ul/li[1]/a/img").click()

a=driver.window_handles
driver.switch_to.window(a[-1])

driver.find_element_by_id("addCart").click()
driver.find_element_by_name("cart1_go").click()

a=driver.window_handles
driver.switch_to.window(a[-1])

driver.find_element_by_name("icart1_ope_buy01").click()


time.sleep(5)
driver.quit()
