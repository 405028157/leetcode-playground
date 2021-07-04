"""
原文章在 https://bytes.com/topic/algorithms/insights/886822-calculating-large-exponents
说一下思路，一个指数的各个位代表的值都是2的指数，比如 n = 13, 二进制是 1101，那么就可以根据各个位看出13 = 8 + 4 + 1，
那个指数的结果就可以表示成(base^8) * (base^4) * (base^1), base的值恰好是从base^1开始，所以n也从最低位开始看，如果最低位是1，说明需要乘上当前的base值，
如果是0，就说明不需要当前的base^some_value来组成最终的结果。每次base都乘自己，1->2->4->8，每次n向右移一位。
"""

# 不取余
def pow(base, n):
    ans = 1
    while n > 0:
        if (n & 1) != 0:
            ans *= base
        base *= base
        n >>= 1
    
    return ans

# 取余
def pow(base, n):
    ans = 1
    while n > 0:
        if (n & 1) != 0:
            ans = (ans % 1000000007) * base
        base = (base * base) % 1000000007
        n >>= 1
    
    return ans % 1000000007


def fast_power(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return  1 / fast_power(x,-n)
    elif n % 2 :#0是false，会执行偶数部分，不会执行下面代码
        return fast_power(x*x,n//2) % 1000000007 * x #奇数的处理方法，原理见下面代码
    else:#偶数部分
        return fast_power(x*x,n//2) % 1000000007