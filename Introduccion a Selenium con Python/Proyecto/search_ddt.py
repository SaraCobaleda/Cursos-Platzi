import csv, unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Importar libreria ddt y extraer submodulos
from ddt import ddt, data, unpack
#Permitira utilizar los datos y desempaquetarlos

#consulta el archivo csv
def get_data(file_name):
    rows = []
    #se abre el archivo en modo lector
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    #indica que pasa a la siguiente fila de datos
    next(reader, None)

    for row in reader:
        rows.append(row)
    return (rows)

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    #aqui estan los terminos que se van a buscar y que se toman del archivo externo
    #unpack es para obtener la informacion
    @data(*get_data('testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        #buscar la barra de busqueda
        search_field = driver.find_element_by_name('q')
        #limpiar la barra de busqueda
        search_field.clear()
        #llamar search_value para mandarlo en la barra de busqueda
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//h2[@class= "product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0:
            #valida que sean iguales
            self.assertEqual(expected_count, len(products))
        else:
            #identifica el titulo y verifica que no hay productos comparando el mensaje
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search retunr no results', message)

        print(f'Found {len(products)} products')
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)