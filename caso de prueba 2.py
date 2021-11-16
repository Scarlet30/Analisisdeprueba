import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
	def test_buscar(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

		usuario = driver.find_element_by_id("email")
		usuario.send_keys("dpmunozpaola@gmail.com")
		usuario.send_keys(Keys.ENTER)
		time.sleep(3)

		clave = driver.find_element_by_id("passwd")
		clave.send_keys("Daniela03")
		clave.send_keys(Keys.ENTER)

		#INGRESO A ORDEN HISTORY
		toggle = driver.find_element_by_xpath("//*[@id='center_column']/div/div[1]/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)

		toggle = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)

		#MY CREDIT SLIP
		toggle = driver.find_element_by_xpath("//*[@id='center_column']/div/div[1]/ul/li[2]/a/span")
		toggle.click()
		time.sleep(3)

		toggle = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)

		#MY ADDRESS
		toggle = driver.find_element_by_xpath("//*[@id='center_column']/div/div[1]/ul/li[3]/a/span")
		toggle.click()
		time.sleep(3)

		toggle = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)

		#MY PERSONAL INFORMATION
		toggle = driver.find_element_by_xpath("//*[@id='center_column']/div/div[1]/ul/li[4]/a/spanspan")
		toggle.click()
		time.sleep(3)

		toggle = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)

		#MY WHISLISTS
		toggle = driver.find_element_by_xpath("//*[@id='center_column']/div/div[2]/ul/li/a/span")
		toggle.click()
		time.sleep(3)

		toggle = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/a/span")
		toggle.click()
		time.sleep(3)


if __name__ =='__main__':
	unittest.main()
