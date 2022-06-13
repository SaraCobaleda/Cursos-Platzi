def run():
    nombre = input("digite su nombre: ")
    for letra in nombre:
        print(letra)
    frase = input("Digite frase: ")
    for caracter in frase:
        print(caracter.upper())


if __name__ == "__main__":
    run()