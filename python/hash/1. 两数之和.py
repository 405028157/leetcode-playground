class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for idx, value in enumerate(nums):
            dic[value] = idx
        
        for idx, value in enumerate(nums):
            t = dic.get(target - value)
            if t and t != idx:
                return [idx, t]
        
        return []
            