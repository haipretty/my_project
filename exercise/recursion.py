def factorial(n):
   if n == 1:
    return n
   else:
    return n*factorial(n-1)

n = int(input("a number: "))
print(f"{n} factorial is",factorial(n))