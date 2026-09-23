def zeroDivision(x, y):
    try:
        result = x/y
        print(f"{x} divided by {y} equals {result}")
    except ZeroDivisionError:
        print("Cannot be divided by Zero")
    except:
        print("There is an error!")
    else:
        print("divide succeed")

def valueError(x):
    try:
        print("What you input is", int(x))
    except ValueError as e:
        print("Error code: ", e)
    except Exception as e:
        print("There is an error!")
    else:
        print("succeed")


#zerodivision(10,0)
#valueError(input("input an integer: "))

cases = int(input())
for _ in range(cases):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

