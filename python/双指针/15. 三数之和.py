"""
排完序后，对每一个固定好的first，second和third用双指针思路就可以。这道题额外需要注意的是，在循环的时候，因为可能有重复的元素，导致重复答案，所以每层循环需要看情况continue
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            left = first + 1
            right = n - 1
            
            while left < right:
                s = nums[first] + nums[left] + nums[right]
                n1 = nums[left]
                n2 = nums[right]
                
                if s == 0:
                    ans.append([nums[first], nums[left], nums[right]])
                
                    # 这里让left和right都一定挪到nums[left], nums[right]不相等的理由是，当 sum = 0时， nums[left]变小，那么nums[right]一定要变大，和才可能再次等于0
                    while left < right and nums[left] == n1:
                        left += 1
                    while left < right and nums[right] == n2:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
                
        return ans