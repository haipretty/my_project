class Solution:
    def isUgly(self, n: int) -> bool:
        flag = True
        while n > 1 and flag:
          flag = False
          if n % 2 == 0:
            n = n / 2
            flag = True
          if n % 3 == 0:
            n = n / 3
            flag = True
          if n % 5 == 0:
            n = n / 5
            flag = True

        if n <= 0:
           return False
        elif n == 1:
           return True
        else:
           return False

myClass = Solution()
print(myClass.isUgly(6))