class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = 0
        dic= {}
        
        for v3 in nums3:
            for v4 in nums4:
                dic[v3 + v4] = dic.get(v3 + v4, 0) + 1
        
        for v1 in nums1:
            for v2 in nums2:
                if -(v1 + v2) in dic:
                    count += dic[-(v1 + v2)]
        
        return count