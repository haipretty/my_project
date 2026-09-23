#to do

import math
def powerSum(X, N):
    number = 0
    leave = X
    lists = []
    if X == 1:
        print("1**N = 1")
        return 1
    for i in range(int(X/2), 0, -1):
        power = i**N
        if power > leave:
            continue
        elif power == leave:
            lists.append(i)
            print(lists)
            number += 1
        else:
            leave -= power
            lists.append(i)
    return number

lists = []
number = 0

def checkPower(X, N):
    leave = X
  
    if X == 1:
        print("1**N = 1")
        return 1
    for i in range(int(X/2), 0, -1):
        power = i**N
        if power > leave:
            continue
        elif power == leave:
            lists.append(i)
            print(lists)
            number += 1
        else:
            leave -= power
            number += checkPower(leave, N)
    return number
#print(math.sqrt(100))
print(powerSum(100,2))