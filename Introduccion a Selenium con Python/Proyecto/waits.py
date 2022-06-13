import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#Herramienta para seleccionar elementos de la web con sus selectores
from selenium.webdriver.common.by import By
#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
#Importar esperar explicitas
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):
        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #espera maximo 10 segundos para encontrar el elemento que esta visible
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        #espera maximo 2 segundos para buscar un elemento cliqueable
        create_account_button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)