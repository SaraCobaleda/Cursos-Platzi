import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        table_data_web = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i + 1}]/span')
            #/html/body/div[2]/div/div/table[1]/thead/tr/th[1]/span
            table_data[i].append(header.text)

            if i < (4):
                web = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{i + 1}]/td[5]')
                table_data_web[i].append(web.text)
                #/html/body/div[2]/div/div/table[1]/tbody/tr[1]/td[5]
                #/html/body/div[2]/div/div/table[1]/tbody/tr[2]/td[5]
                #/html/body/div[2]/div/div/table[1]/tbody/tr[3]/td[5]
                #/html/body/div[2]/div/div/table[1]/tbody/tr[4]/td[5]

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j + 1}]/td[{i + 1}]')
                #/html/body/div[2]/div/div/table[1]/tbody/tr[3]/td[1]
                table_data[i].append(row_data.text)
        
        print(table_data)
        print('/'*100)
        print(table_data_web)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)