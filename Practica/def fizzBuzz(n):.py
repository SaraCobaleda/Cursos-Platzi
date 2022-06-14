def fizzBuzz(n):
    for i in range (n+1):
        if (i != 0):
            if (i % 3 == 0 and i % 5 != 0):
                print ("Fizz")
            elif (i % 5 == 0 and i % 3 != 0):
                print ("Buzz")
            elif (i % 3 == 0 and i % 5 == 0):
                print ("FizzBuzz")
            else:
                print(i)
    # Write your code here

if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)