import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from webdriver_manager.chrome import ChromeDriverManager

class SearchTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        #limpia el campo de búsqueda en caso de que haya algún texto.

        search_field.send_keys('tee')
        #enviamos la palabra tee al campo de busqueda
        search_field.submit()  
        #envía los datos ('tee') para que la página muestre los resultados de "tee"

    def test_search_salt_chaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('salt shaker')
        #escribimos 'salt shaker' en la barra de búsqueda
        search_field.submit
        #envíamos la petición

        #hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
        products = driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        #pregunta si la cantidad de resultados es igual a 1
        self.assertEqual(1, len(products))


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)