"""
把这道题想象成有一个容量为sum(nums) / 2的背包，看看能不能正好把这个背包填满
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)
        if total % 2 == 1 or n == 1:
            return False
        
        C = total >> 1
        dp = [[0] * (C + 1) for _ in range(n + 1)]
        for i in range(1, C + 1):
            dp[0][i] = float('-inf')
        
        for i in range(0, n + 1):
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, C + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
        
        return dp[n][C] != float('-inf')