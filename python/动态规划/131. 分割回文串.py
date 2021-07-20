class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []
        ret = []
        f = [[True] * n for _ in range(n)] # 一会再处理

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
    
        def dfs(i: int):
            if i >= n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret