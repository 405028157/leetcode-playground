class Solution:
    # @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        t1 = 0
        t2 = 1
        t3 = 1

        for i in range(n - 2):
            temp = t1 + t2 + t3
            t1 = t2
            t2 = t3
            t3 = temp
        
        return t3