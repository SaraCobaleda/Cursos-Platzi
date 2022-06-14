class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color 
        self._estado = 'en reposo' #variabl privada
        self._motor = Motor(cilindros = 4) #varible privada

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'


class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'):
        #tipo es un parametro llamado default keyword
        self.cilindros = cilindros
        self.tipos = tipo
        self._temperatura = 0 #variable privada

    def inyecta_gasolina(self, cantidad):
        pass