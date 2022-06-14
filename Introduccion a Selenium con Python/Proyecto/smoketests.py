from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
#para generar el reporte
from assertions import AssertionsTest
from testsearch import SearchTest

asserttions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

#contruimos la suite de pruebas
smoke_test = TestSuite([asserttions_test, search_test])

#para generar los reporters
kwargs = {
    "output": 'smoke-report'
}

#la variable runner almacena un reporte generado por HTMLTestRuner, usa como argumento "kwarsp"
runner = HTMLTestRunner(**kwargs)
#corro el runner con la suite de prueba
runner.run(smoke_test)