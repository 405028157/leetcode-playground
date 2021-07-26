"""
dp[i][0] 数组nums[0, ... i]最大乘积
dp[i][1] 数组nums[0, ... i]最小乘积，主要是负数

dp[i][0] = max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])
dp[i][1] = min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i], nums[i])

空间压缩
dp[0] = max(dp[0] * nums[i], dp[1] * nums[i], nums[i])
dp[1] = min(dp[0] * nums[i], dp[1] * nums[i], nums[i])
"""
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_ans = float('-inf')
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0] * nums[1], 0, nums[0], nums[1])

        dp = [0, 0]
        dp[0] = max(0, nums[0])
        dp[1] = min(0, nums[0])
        max_ans = max(dp[0], max_ans)    

        for i in range(1, n):
            # print(dp)
            dp[0], dp[1] = max(dp[0] * nums[i], dp[1] * nums[i], nums[i]), min(dp[0] * nums[i], dp[1] * nums[i], nums[i])
            max_ans = max(dp[0], max_ans)
        
        # print(dp)
        return max_ans