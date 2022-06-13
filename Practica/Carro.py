from keyring import set_password


def calcularMaximoRetorno(instruccion):
    p = 0
    ans = []
    for t in instruccion:
        
        Movimiento = []
        for i in instruccion[p]:
            Movimiento.append(i)
        
        contx = 0
        conty = 0
        maxx = 0
        maxy = 0

        for i in Movimiento:
            if (i == 'R'):
                contx = contx + 1
            elif (i == 'L'):
                contx = contx - 1
            elif (i == 'U'):
                conty = conty + 1
            elif (i == 'D'):
                conty = conty - 1

            print (contx, conty)

            if (maxx < abs(contx)):
                maxx = abs(contx)
            if (maxy < abs(conty)):
                maxy = abs(conty)

            print('valores', maxx, maxy)

        

        p = p+1

        cont = maxx + maxy
        
        R = str(cont)
        ans.append(R)

    return (ans)
    # Write your code here

if __name__ == '__main__':

    instruccion = ['RUULLLDDDR']

    result = calcularMaximoRetorno(instruccion)
    print(result)