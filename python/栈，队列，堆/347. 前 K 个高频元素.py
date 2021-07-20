import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        q = []
        for key, value in dic.items():
            q.append((-value, key))
        
        heapq.heapify(q)
        for _ in range(k):
            res.append(heapq.heappop(q)[1])
        
        return res