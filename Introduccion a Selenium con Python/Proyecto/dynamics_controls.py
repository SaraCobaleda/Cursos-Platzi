import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamics_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()
        print('########### 1 ##########')

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()
        print('########### 2 ##########')

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()
        print('########### 3 ##########')

        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()
        print('########### 4 ##########')

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        print('########### 5 ##########')
        
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Platzi')
        print('########### 6 ##########')

        enable_disable_button.click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)