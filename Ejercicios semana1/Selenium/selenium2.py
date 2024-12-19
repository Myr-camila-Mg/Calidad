from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from time import sleep
from selenium.webdriver.common.by import By

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_campus(self):
		browser = self.browser
		browser.get(" https://campusvirtualunillanos.co/ ")
		activos= browser.find_element(By.XPATH,'//*[@id="numbers"]/div/div/div[2]/div/div[1]/div/h3')
		cursos= browser.find_element(By.XPATH,'//*[@id="numbers"]/div/div/div[2]/div/div[2]/div/h3')
		print("Usuarios activos: " + activos.text)
		print("Cursos: " + cursos.text)
		
	def tearDown(self):
		print()
		#self.browser.quit()
		

if __name__ == '__main__':
	unittest.main()