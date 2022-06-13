import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HiWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(1000)

    def test_Hi_World(self):
        self.driver.get('https://www.facebook.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hi_wold_report'))