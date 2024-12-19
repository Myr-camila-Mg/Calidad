from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://google.com/")
time.sleep(2) #Mostrar despues
browser.get("http://demo.guru99.com/test/login.html")
browser.execute_script("window.open('');")
browser.execute_script("window.open('');")
browser.execute_script("window.open('');") 
browser.switch_to.window(browser.window_handles[1]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[2]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[3]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[0]) 
time.sleep(2)
browser.quit()


try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()