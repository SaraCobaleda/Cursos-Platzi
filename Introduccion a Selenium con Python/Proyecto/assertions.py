import unittest
from selenium import webdriver
#sirve como excepción para los assertions cuando queremos
#validar la presencia de un elemento
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
#llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_languaje_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-languaje'))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    #para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity = 2)