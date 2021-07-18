class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total, n = sum(stones), len(stones)
        C = total >> 1

        # dp = [False for _ in range(C + 1)]
        # dp[0] = True

        dp = [0 for _ in range(C + 1)]

        for i in range(1, n + 1):
            for j in range(C, stones[i - 1] - 1, -1):
                # j 在范围 [0, nums[i - 1])时，dp[j] = dp[j]，等于不用更新
                dp[j] = max(dp[j], dp[j - stones[i - 1]] + stones[i - 1])
        
        return abs(total - dp[C] - dp[C])
        
        