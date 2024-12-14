# -*- coding: utf-8 -*-
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
		browser.get("https://www.unillanos.edu.co/")
		campus = browser.find_element(By.XPATH, '//*[@id="jm-top-bar1"]/div[1]/div/p[1]/strong[1]/a')
		campus.send_keys(Keys.ENTER)
		browser.execute_script("window.open('');") #Carga en background el primero
		time.sleep(3)
		browser.switch_to.window(browser.window_handles[1]) #Para abrir una ventana nueva 1, porque ya se abrio la cero
		time.sleep(3)
		acceder= browser.find_element(By.XPATH,'//*[@id="usernavigation"]/div[4]/div/span/a')
		acceder.send_keys(Keys.ENTER)
		username = browser.find_element(By.ID, 'username')
		username.clear()
		username.send_keys('161004323')
		contrasena = browser.find_element(By.ID, 'password')
		contrasena.clear()
		contrasena.send_keys('12Sunny18')
		submitButton = browser.find_element(By.ID, 'loginbtn')
		submitButton.send_keys(Keys.ENTER)
		sleep(2)
		res = browser.find_element(By.XPATH, '//*[@id="page-header"]/div[2]/h2')
		self.assertEqual('¡Hola, MYRIAM CAMILA! 👋', res.text)
	
	def tearDown(self):
		print()
		#self.browser.quit()
		

if __name__ == '__main__':
	unittest.main()