class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        n = len(nums)

        for l in range(1, n + 1):
            for start in range(0, n):
                if start + l <= n:
                    res.append(nums[start: start + l])
        
        return res