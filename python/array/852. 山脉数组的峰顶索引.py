class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        max_num = 0
        index = 0

        for i in range(n):
            if arr[i] > max_num:
                max_num = arr[i]
                index = i
        
        if index == 0 or index == n - 1:
            return False
        return index