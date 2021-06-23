class Solution:
    def permutation(self, s: str) -> list[str]:
        ans = []
        n = len(s)
        # print(f's = {s}, len(s) = {len(s)}')
        visited = {}

        def dfs(path: str):
            # print(f'path = {path}, n = {n}, len(path) = {len(path)}')
            if len(path) == n:
                # 注意这里，如果path是数组，一定要切片 path[:]来copy一份，这里因为是字符串，所以不会产生引用重复结果的问题
                ans.append(path)
                return

            for i in range(n):
                if not visited.get(i, False):
                    if i > 0 and s[i - 1] == s[i] and visited.get(i - 1, False) == True:
                        continue
                    visited[i] = True
                    dfs(path + s[i])
                    visited[i] = False
        
        s = ''.join(sorted(list(s)))
        dfs('')
        return ans