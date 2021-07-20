class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return sum(nums)
        nums.sort()
        max_sum = float('-inf')

        """
        n = 4
        0, 3
        1, 2
        """
        for i in range(0, n >> 1):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
        
        return max_sum