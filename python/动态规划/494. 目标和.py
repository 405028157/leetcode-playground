"""
dp[i][j]，使用nums中i个数，和为target的方案数
dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
"""

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ans = 0

        dp = [[0] * 3001 for _ in range(n + 1)]

        dp[0][0 + 1000] = 1
        
        for i in range(0, 1000):
            dp[0][i] = 0
        
        for i in range(1001, 3001):
            dp[0][i] = 0
        
        # i 和 j的range都正常写，在访问dp的时候，再对j+1000
        for i in range(1, n + 1):
            for j in range(-1000, 1001):
                dp[i][j + 1000] = dp[i - 1][j - nums[i - 1] + 1000] + dp[i - 1][j + nums[i - 1] + 1000]

        return dp[n][target + 1000]


"""
https://leetcode-cn.com/problems/target-sum/solution/494-mu-biao-he-dong-tai-gui-hua-zhi-01be-78ll/
更好的思路，以及空间优化 -> 装满背包有多少种方案
"""
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1 or total < target:
            return 0

        C = (total + target) >> 1
        dp = [0 for _ in range(C + 1)]
        dp[0] = 1
    
        n = len(nums)
        
        for i in range(1, n + 1):
            for j in range(C, nums[i - 1] - 1, -1):
                # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                dp[j] = dp[j] + dp[j - nums[i - 1]]
        # print(dp)
        return dp[C]


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