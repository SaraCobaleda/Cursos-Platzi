import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)
    #O(n) * O(n) = O(n**2)
    for i in range(n):
        for j in range(0, n - i - 1):
             if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista 


if __name__ == '__main__':
    tamano_de_la_lista = int(input('De que tamano sera la lista? '))
    
    lista = [random.randint(0, 100) for i in range (tamano_de_la_lista)]
    print(f'La lista no ordenada es {lista}')

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(f'La lista ordenada es {lista_ordenada}')
    