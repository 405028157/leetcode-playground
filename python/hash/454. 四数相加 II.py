class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = 0
        for v1 in nums1:
            for v2 in nums2:
                for v3 in nums3:
                    for v4 in nums4:
                        if v1 + v2 + v3 + v4 == 0:
                            count += 1
        return count