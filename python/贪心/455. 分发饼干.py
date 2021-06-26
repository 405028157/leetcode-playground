"""
pop操作其实不需要，可以用下标前进来模拟
"""

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        num = 0

        while s:
            # 每次找到一个满足g[0]的s元素
            while s and g and s[0] < g[0]:
                s.pop(0)
            # 如果存在
            if s and g:
                s.pop(0)
                g.pop(0)
                num += 1
            # 任何一个为空了，就打住了
            else:
                return num
        
        return num

"""
用下标前进来模拟
def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if not (g and s):
            return 0

        s.sort()
        g.sort()
        num = 0

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        
        return i
"""