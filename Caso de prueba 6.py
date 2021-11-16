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

		EmailAddressCreate = driver.find_element_by_id("email_create")
		EmailAddressCreate.send_keys("alguncorreo@gmail.com") #cuenta no esta registrada
		time.sleep(3)
		toggle = driver.find_element_by_xpath("//*[@id='SubmitCreate']")
		toggle.click()
		time.sleep(3)

		radio_bt = driver.find_element_by_xpath("//*[@id='id_gender2']")
		radio_bt.click()
		time.sleep(3)

		FirtName = driver.find_element_by_xpath("//*[@id='customer_firstname']")
		FirtName.send_keys("Nombre de prueba")
		time.sleep(3)

		LastName = driver.find_element_by_id("customer_lastname")
		LastName.send_keys("Apellido de prueba")
		time.sleep(3)

		Password = driver.find_element_by_id("passwd")
		Password.send_keys("Nomb1")
		time.sleep(3)

		select = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select")
		select.send_keys("1")

		selectmes = driver.find_element_by_name("months")
		selectmes.send_keys("January")

		selectyears = driver.find_element_by_name("years")
		selectyears.send_keys("2021")
		time.sleep(3)

		address1 = driver.find_element_by_id("address1")
		address1.send_keys("Cl 1 # 1 - 1")
		time.sleep(3)		

		City = driver.find_element_by_id("city")
		City.send_keys("Ciudad")
		time.sleep(3)		

		selectstate = driver.find_element_by_xpath("//*[@id='id_state']")
		selectstate.send_keys("Arizona")
		time.sleep(3)

		CodigoPostal = driver.find_element_by_id("postcode")
		CodigoPostal.send_keys("36523")
		time.sleep(3)	

		PhoneMobile = driver.find_element_by_id("phone_mobile")
		PhoneMobile.send_keys("123456789")
		time.sleep(3)	

		Alias = driver.find_element_by_id("alias")
		Alias.send_keys("AliasEscrito")
		time.sleep(3)




if __name__ =='__main__':
	unittest.main()