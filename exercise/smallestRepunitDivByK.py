class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        length = 1
        n = 1
        digit = 1
        while length < 10**10:
            if n % k == 0:
                return length
            else:
                #n = int(str(n)+"1")
                length += 1
                digit *= 10
                n += digit
        return -1