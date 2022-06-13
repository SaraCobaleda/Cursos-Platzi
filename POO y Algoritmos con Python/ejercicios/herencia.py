
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    #la clase cuadrado extiende a rectangulo

    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())

    #la clase cuadrado hereda el metodo area de la super clase
    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())
