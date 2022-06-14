# coding = utf-8
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Firefox () Abra el navegador Firefox
driver = webdriver.Chrome(ChromeDriverManager().install())   # Abrir Chrome
driver.maximize_window()    # Maximiza la ventana
driver.get('https://www.facebook.com')    # Dirección abierta
time.sleep(60)    # Sleep60s
driver.refresh()    # Actualizar la página abierta
driver.close()     #Cerrar el navegador