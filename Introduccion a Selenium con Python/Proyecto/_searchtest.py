import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomaPageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        nutton = self.driver.find_element_by_class_name('button')

    def test_count_or_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_element_by_tag_name('img')
        #self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vio_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')

    def test_shopping_cart(self):
        shoping_cart_icon = self.driver.find_elements_by_css_selector('dev.header-minicart span.icon')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)