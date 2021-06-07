class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            third = n - 1
            for second in range(first + 1, n - 1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                
                if second == third:
                    break
                
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans