def divisors(num):
    try:
        if num<0 or num==0:
            raise ValueError("No se pueden ingresar numeros negativos o 0")
        # divisors = []
        # for i in range(1, num + 1):
        #     if num % i == 0:
        #         divisors.append(i)
        divisors = [x for x in range(1, num + 1) if num%x==0]
        return divisors
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Porfavor ingresa un numero. ")


if __name__ == '__main__':
    run()