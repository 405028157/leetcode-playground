class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combination = []
        ans = []

        def dfs(cur: int):
            # print(cur)
            if len(combination) == k:
                # print('a')
                ans.append(combination[:])
                return
            
            # 剪枝
            if len(combination) + (n - cur) < k:
                # print('b')
                return

            # [cur+1, cur+2, ..., n]
            for i in range(cur + 1, n + 1):
                combination.append(i)
                dfs(i)
                combination.pop()
        
        dfs(0)
        return ans
                

        