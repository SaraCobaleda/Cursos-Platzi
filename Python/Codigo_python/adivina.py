import random

def run():
    numero_al = random.randint(1, 100)
    numero_el = int(input("Elige un numero del 1 al 100: "))
    while numero_el != numero_al:
        if numero_el < numero_al:
            print("Busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño ")
        numero_el = int(input("Elige otro numero: "))
    print("ganaste! ")

if __name__ == "__main__":
    run()