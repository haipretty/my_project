def fibo(n):
    if n <= 0:
        print("Please input number geater than 0")
    elif n <= 2:
        return n-1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(4))