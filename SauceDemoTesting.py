import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\marya\\Documents\\Driver2\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://saucedemo.com")
driver.implicitly_wait(5)
#Login
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
driver.find_element(By.NAME, 'login-button').click()

#AddToCart
dropdown = Select(driver.find_element(By.CSS_SELECTOR, '.product_sort_container'))
dropdown.select_by_index(1)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

#CheckOut
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.NAME, "firstName").send_keys("Deem")
driver.find_element(By.ID, "last-name").send_keys("Meed")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("3456")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
time.sleep(2)
driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()


