

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0
        
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    print(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n-1))
    print('-' * 30)
    print(morral(tamano_morral, pesos, valores, n-1))

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n-1), 
        morral(tamano_morral, pesos, valores, n-1))


if __name__ == '__main__':
    valores = [60, 100, 120, 300]
    pesos = [10, 20, 30, 40]
    tamano_morral = 15
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)