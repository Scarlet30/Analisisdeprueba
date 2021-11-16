from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
time.sleep (20)
driver.close()
