"""
排完序后，对每一个固定好的first，second和third用双指针思路就可以。这道题额外需要注意的是，在循环的时候，因为可能有重复的元素，导致重复答案，所以每层循环需要看情况continue
"""
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
                
                # 这里只需要找到一个third就好了，因为third再往左要么就是大小相同的重复结果，要么就是变小使和 < 0
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans