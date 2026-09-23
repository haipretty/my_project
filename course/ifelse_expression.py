def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

num = int(input("input a number: "))
print("Yes" if is_prime(num) else "No")