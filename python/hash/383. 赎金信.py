class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        dic_a = Counter(ransomNote)
        dic_b = Counter(magazine)

        for key, value in dic_a.items():
            if value > dic_b[key]:
                return False
        
        return True

s = Solution()
s.canConstruct('aa', 'aab')