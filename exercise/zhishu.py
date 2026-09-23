import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        zhishu = [True]*n
        zhishu[0] = zhishu[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if zhishu[i]:
                for j in range(i*i, n, i):
                    zhishu[j] = False

        return sum(zhishu)

    def is_prime(n):
        if n <= 1:
            return "Not prime"
        else:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return "Not prime"
            return "Prime"

s1 = Solution()
print(s1.countPrimes(499979))
