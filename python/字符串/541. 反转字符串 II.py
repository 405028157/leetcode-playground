class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        s = list(s)
        while left + k < n:
            # k 个数，应该是[left, ..., left + k - 1]
            i, j = left, left + k - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            left += 2 * k
        
        if left < n:
            i, j = left, n - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return ''.join(s)