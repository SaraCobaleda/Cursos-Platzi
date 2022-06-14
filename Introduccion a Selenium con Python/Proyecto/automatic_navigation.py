import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class NavigacionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        driver.back()#retroceder navegador
        sleep(1)
        driver.forward()#avanzar
        sleep(1)
        driver.refresh()# actualizar página
        sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)