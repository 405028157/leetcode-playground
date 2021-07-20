"""
超出时间限制
"""

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        ans = 0
        

        def dfs(rest:int):
            nonlocal ans
            if rest == 0:
                ans += 1
                return

            # 题目没说整数不可以是负数，先当做不可以吧
            if rest < 0:
                return

            for num in nums:
                dfs(rest - num)
        
        dfs(target)
        return ans
            
                
"""
动态规划，正确思路

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        n = len(nums)
        nums.sort()

        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(n):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
                else:
                    break
        
        return dp[target]
"""