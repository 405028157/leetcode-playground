class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)
        dic = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
        res = []

        def dfs(combination: str, index: int):
            if index >= n:
                return
            
            if index == n - 1:
                for c in dic[digits[index]]:
                    res.append(combination + c)
                return
            
            for c in dic[digits[index]]:
                dfs(combination + c, index + 1)
        
        dfs('', 0)
        return res