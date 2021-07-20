"""
错误：1. 审题错了，不是找到四个数让和=0，是让和=target
2. 建字典的时候，让和为同一个数的一对[a, b]不能出现俩次，导致漏了原本可能dic[sum] = [[index_a, index_b], [indexc, indexd]]的下标

可以用哈希想办法把时间复杂度降到O(n^2)，不过官方答案就给了O(n^3)的解法
"""
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        dic = {}
        nums.sort()
        ans = []
        n = len(nums)
        print(nums)
        
        
        """
        1,0,-1,0,-2,2,3,4,-4
        dic[sum] = [indexA, indexB]
        dic[3] = [[1, 5], [2, 6]]
        """

        # O(n^2)
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 可以保证和为nums[i] + nums[j]的俩数和之前的不同
                s = nums[i] + nums[j]
                if s in dic:
                    dic[s].append([i, j])
                else:
                    dic[s] = [[i, j]]
                
        
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                if -(nums[first] + nums[second]) in dic:
                    for i, j in dic[-(nums[first] + nums[second])]:
                        print(f'first = {first}, second = {second}, i = {i}, j = {j}')
                        print(f'nums[first] = {nums[first]}, nums[second] = {nums[second]}, nums[i] = {nums[i]}, nums[j]  = {nums[j]}')
                        if i > second:
                            ans.append([nums[first], nums[second], nums[i], nums[j]])
        
        return ans
        