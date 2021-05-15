"""
使用的左闭右闭区间二分[left, right]，while使用left < right
需要找到第一个大于等于target的数的下标，所以小于target的区间肯定是无用的
"""
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            print(f'left={left}, right={right}')
            mid = (left + right) // 2
            if nums[mid] < target: #排除掉不想要的区间
                left = mid + 1
            else: # nums[mid] > target，或者nums[mid] == target，我们去缩减这个区间
                right = mid
        return left

s = Solution()
print(s.searchInsert([1,3,5,6], 7))