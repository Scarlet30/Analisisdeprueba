from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://automationpractice.com/index.php?controller=contact")


EmailAddress = driver.find_element_by_id("email")
EmailAddress.send_keys("dpmunozpaola@gmail.com")
EmailAddress.send_keys(Keys.ENTER)
time.sleep(3)

OrdenReference = driver.find_element_by_id("id_order")
OrdenReference.send_keys("123456787")
OrdenReference.send_keys(Keys.ENTER)
time.sleep(3)

Message = driver.find_element_by_id("message")
Message.send_keys("Aqui va el mensaje")
Message.send_keys(Keys.ENTER)
time.sleep(3)
