def busquedaB(objetivo):
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    return respuesta
    
def aproximacion(objetivo):
    print('soy la opcion 0')
    epsilon = 0.1
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    return respuesta 

funcion = int(input('Escoge opcion: '))
numero = int(input('Escoge un numero: '))

opciones = {
        1 : busquedaB(numero),
        2 : aproximacion(numero)
    }

print(opciones[1])