inputArray = [-23, 4, -3, 8, -12]

max = -999999
next = 1
for i in inputArray:
    if next < len(inputArray):
        if max < i * inputArray[next]:
            max = i * inputArray[next]
    next += 1
print(max)