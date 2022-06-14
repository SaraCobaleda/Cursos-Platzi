import unittest
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add? '))
        elements_removed = int(input('How many elements will you remove? '))

        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('You are trying to DELETE more elements than the existent')
                break
        
        if total_elements > 0:
            print(f"there are {total_elements} elements on the screen")
        else:
            print("there are 0 elements on the screen")

        sleep(3)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)