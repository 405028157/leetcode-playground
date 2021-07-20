class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        combination = []

        def dfs(cur: int, sum: int):
            if len(combination) == k:
                if sum == 0:
                    ans.append(combination[:])
                return
            
            if cur > 9:
                return
            
            # 剪枝
            if sum <= 0:
                return
            
            combination.append(cur)
            dfs(cur + 1, sum - cur)
            combination.pop()
            dfs(cur + 1, sum)
        
        dfs(1, n)

        return ans