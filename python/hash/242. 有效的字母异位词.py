class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        
        for i in t:
            if not dic.get(i):
                return False
            
            dic[i] -= 1
        
        # print(dic)
        # print(dic.values())
        for v in dic.values():
            if v != 0:
                return False
        
        return True