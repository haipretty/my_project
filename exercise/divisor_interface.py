import math

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        super().__init__()
        self.sum = 0

    def divisorSum(self, n):
        n_sqrt = math.sqrt(n)
        for i in range(1, int(n_sqrt)+1):
            if n % i == 0:
                if i**2 == n:
                    self.sum += i
                else:
                    self.sum += i + (n//i)
        return int(self.sum)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)