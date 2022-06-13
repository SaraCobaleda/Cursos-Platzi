from time import sleep
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()

    def test_search(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('platstation4')
        search_field.submit()

        location = driver.find_element_by_xpath('//div/div/aside/section[2]/dl[9]/dd[1]/a')
        location.click()
        sleep(1)

        #condition = driver.find_element_by_partial_link_text('Nuevo')
        #condition.click()
        #sleep(1)

        #order_menu = driver.find_element_by_class_name('ui-dropdown__link')
        #order_menu.click()
        #higer_price = driver.find_element_by_css_selector('a.andes-list__item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
        #higer_price.click()
        #sleep(1)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2')
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            prices.append(article_price)

        print('//'*100)
        print(article_price, prices)


    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)