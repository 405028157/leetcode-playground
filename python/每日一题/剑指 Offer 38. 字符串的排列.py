"""
输入：
"aab"
输出：
[]
预期结果：
["aba","aab","baa"]
"""
class Solution:
    def permutation(self, s: str) -> list[str]:
        dic = {}
        n = len(s)

        def dfs(s: str, path: list[str]):
            if len(path) == n and ''.join(path) not in dic:
                dic[''.join(path)] = True
            for c in s:
                if c not in path:
                    path.append(c)
                    dfs(s, path)
                    path.pop()
        
        dfs(s, [])

        return [l for l in dic.keys()]