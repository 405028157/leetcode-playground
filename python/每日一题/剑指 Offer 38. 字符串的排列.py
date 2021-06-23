class Solution:
    def permutation(self, s: str) -> list[str]:
        ans_s = set()
        n = len(s)
        # print(f's = {s}, len(s) = {len(s)}')
        visited = {}

        def dfs(path: str):
            # print(f'path = {path}, n = {n}')
            if len(path) == n:
                ans_s.add(path)
                return

            for i in range(n):
                if visited.get(i, False):
                    continue
                visited[i] = True
                dfs(path + s[i])
                visited[i] = False
        
        dfs('')
        return list(ans_s)