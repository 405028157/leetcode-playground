class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combination = []
        ans = []

        def dfs(cur: int):
            if len(combination) == k:
                ans.append(combination[:])
                return
            
            # 每层做下层的决定，所以 cur > n，说明到最底层了
            if cur > n:
                return
            
            # 剪枝
            # [cur, ..., n]
            if n - cur + 1 + len(combination) < k:
                return
            

            combination.append(cur)
            dfs(cur + 1)
            combination.pop()
            dfs(cur + 1)
        
        dfs(1)
        return ans