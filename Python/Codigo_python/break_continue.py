def run():
#   for contador in range(1000):
#       if contador %2 != 0:
#           continue
#       print (contador)
    
#   for i in range (10000):
#       print(1)
#       if i == 5768:
#           break

    texto = input("escribe texto: ")
    for caracter in texto:
        if caracter == "o":
            break
        print(caracter)



if __name__ == "__main__":
    run()