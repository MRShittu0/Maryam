import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\marya\\Documents\\Driver2\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")


driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
Text = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
#var = message.split("at")[1].strip().split(" ")[0]
print(Text)
email = driver.find_element(By.XPATH, "//a[normalize-space()='mentor@rahulshettyacademy.com']").text
print(email)

driver.switch_to.window(windows[0])
driver.find_element(By.NAME, "username").send_keys(email)
driver.find_element(By.NAME, "password").send_keys("learnning")
driver.find_element(By.XPATH, "(//span[@class='checkmark'])[1]").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_index(2)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
time.sleep(2)
alert = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text
print(alert)
