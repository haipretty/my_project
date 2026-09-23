
x, y = map(int, input().split())
print(eval("x == y"))    #eval执行str中的代码

#定义运算符字典
operators = {
    '+':lambda x,y:x+y,
    '-':lambda x,y:x-y,
    '*':lambda x,y:x*y,
    '/':lambda x,y:x/y,
    '//':lambda x,y:x//y,
    '**':lambda x,y:x**y
}

# x, op, y = input().split()
# res = operators[op](int(x), int(y))
# print(res)