"""
dp[i][j]，使用nums中i个数，和为target的方案数
dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
"""

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ans = 0

        dp = [[0] * 2001 for _ in range(n + 1)]

        dp[0][0 + 1000] = 1
        
        for i in range(0, 1000):
            dp[0][i] = 0
        
        for i in range(1001, 2001):
            dp[0][i] = 0
        
        for i in range(1, n + 1):
            for j in range(1001, target + 1001):
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
        return dp[n][target + 1000]
        

"""
回溯 超时
"""
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ans = 0
        def dfs(index, cur_sum):
            # print(f'cur_sum = {cur_sum}, index = {index}')
            nonlocal ans
            if index == n:
                if cur_sum == target:
                    ans += 1
                    # print('ans += 1')
                return
            
            dfs(index + 1, cur_sum - nums[index])
            dfs(index + 1, cur_sum + nums[index])
        
        dfs(0, 0)
        return ans