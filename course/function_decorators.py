def dec(func):
    print("dec")            #1
    def inner():
        print("inner")      #4
        print(func().lower())   #在这里调用myName方法，#6
        print("inner2")     #7
        return "SUCCESS"        #最终myName函数的返回值
    print("dec2")           #2
    return inner        #返回新函数

@dec
def myName():
    print("myName")     #5
    return "Alps"

print("print")          #3
print(myName())         #8


#timeit装饰器
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"take {exec_time:.8f} seconds.")
        return result
    return wrapper