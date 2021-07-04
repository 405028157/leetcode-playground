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