import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
	def test_buscar(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php")
		self.assertIn("My Store", driver.title)
		elemento = driver.find_element_by_id("search_query_top")
		elemento.send_keys("DRESSES")
		elemento.send_keys(Keys.RETURN)
		time.sleep (5)
		assert "No se encontro el elemento:" not in driver.page_source

#	def tearDown(self):
#		self.driver.close()

if __name__ =='__main__':
	unittest.main()
