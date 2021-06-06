class Solution:
    def isHappy(self, n: int) -> bool:
        # 注意l是各位数字的逆序，不过这个题不重要，如果需要逆序，l = l[::-1]就可
        def int_to_array(n: int):
            l = []
            while n:
                l.append(n % 10)
                n //= 10
            return l
        def get_sum(n: int):
            A = int_to_array(n)
            sum = 0
            for i in A:
                sum += i ** 2
            return sum
        dic = {}
        sum = 0
        while sum != 1:
            sum = get_sum(n)
            # print(f'sum = {sum}')
            if dic.get(sum):
                return False
            dic[sum] = 1
            n = sum
        return True
