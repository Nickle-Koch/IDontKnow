from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")
elem = driver.find_element_by_name("search_query")
elem.send_keys("uwu copypasta", Keys.RETURN)

elem2 = driver.find_element_by_id("dismissible")
elem2.click()

