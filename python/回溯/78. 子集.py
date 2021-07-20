class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)

        def dfs(combination: list[int], index: int):
            if index >= n:
                res.append(combination[:])
                return
            
            dfs(combination[:], index + 1)
            dfs(combination + [nums[index]], index + 1)
        
        dfs([], 0)
        return res