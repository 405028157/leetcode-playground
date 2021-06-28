"""
状态压缩+前缀异或和
"""

from collections import Counter

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dic = Counter([0])
        ans = 0
        mask = 0

        for ch in word:
            step = ord(ch) - ord('a')
            mask ^= (1 << step)
            if mask in dic:
                ans += dic[mask]
            for i in range(10):
                pre_mask = mask ^ (1 << i)
                if pre_mask in dic:
                    ans += dic[pre_mask]
            dic[mask] += 1
        
        return ans