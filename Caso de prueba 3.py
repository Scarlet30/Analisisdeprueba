from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")


usuario = driver.find_element_by_id("email")
usuario.send_keys("dpmunozpaola@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_id("passwd")
clave.send_keys("Daniela03")
clave.send_keys(Keys.ENTER)

toggle = driver.find_element_by_xpath("//*[@id='SubmitCreate']")
toggle.click()
time.sleep(3)


