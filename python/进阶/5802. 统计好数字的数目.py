class Solution:
    def countGoodNumbers(self, n: int) -> int:
        is_odd = n % 2 == 1
        even_digit = (n + 1) // 2
        odd_digit = (n - 1) // 2 if is_odd else n // 2
        ans = 1
        
        # (5 ** even_digit) * (4 ** odd_digit)
        
    
        def pow(base, n):
            ans = 1
            while n > 0:
                if (n & 1) != 0:
                    ans = (ans % 1000000007) * base
                base = (base * base) % 1000000007
                n >>= 1

            return ans
        
        return ((pow(5, even_digit) % 1000000007) * (pow(4, odd_digit) % 1000000007)) % 1000000007


"""
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        od = n >> 1
        ev = n - od
        ans = pow(5, ev, 1000000007) * pow(4, od, 1000000007) % 1000000007
        return ans
"""