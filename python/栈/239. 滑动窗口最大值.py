class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        window = []
        for i in range(k):
            window.append(nums[i])
        
        res.append(max(window))
        for i in range(k, n):
            temp = window[0]
            window = window[1:]
            window.append(nums[i])
            if temp == res[-1]:
                res.append(max(window))
            else:
                res.append(max(res[-1], nums[i]))
        
        return res