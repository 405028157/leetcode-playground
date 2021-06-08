"""
>>> s
['f', 's', 'd', 'a', 'f', 'd', 's', 'a']
>>> len(s)
8
>>> s[7:10]
['a']

用到了切片的终点可以超出长度
"""
class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)