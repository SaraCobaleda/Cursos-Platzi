
def podraCumplir(caso):
    p = 0
    Ans = []
    for i in caso:
        objetivo = []
        if (p > 1):
            objetivo = i.split(sep=' ')
            deadline = int(objetivo[0])
            func = int(objetivo[1])
            funcR = int(objetivo[2])
            funcDel = int(objetivo[3])
            result = ((deadline-1)*funcR)-((deadline-1)*funcDel)+funcR
            if(result<func):
                Ans.append('0')
            else:
                Ans.append('1')
        p = p + 1
        print(Ans)
    return(Ans)
    # Write your code here

if __name__ == '__main__':
    caso = ['1','2','2 40 20 5', '5 110 30 10']
    result = podraCumplir(caso)
    print(result) 