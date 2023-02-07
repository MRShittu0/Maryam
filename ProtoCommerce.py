import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\marya\\Documents\\Driver2\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

driver.find_element(By.NAME, "name").send_keys("Dee")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys('dee@gmail.com')
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("3456")
time.sleep(5)
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
time.sleep(2)
dropdown.select_by_visible_text('Male')
time.sleep(2)
dropdown.select_by_visible_text("Female")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
alert = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
print(alert)
