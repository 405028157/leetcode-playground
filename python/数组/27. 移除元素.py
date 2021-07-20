"""
双指针，i慢的那个，j快的那个
"""
class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i