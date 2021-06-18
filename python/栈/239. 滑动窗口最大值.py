"""
heapq 用列表来维护堆，l[0]就是堆顶
"""
import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]

        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        
        return res