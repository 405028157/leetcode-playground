"""
前缀和
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
需要注意的是，从左往右边更新边计算的时候已经保证了\textit{mp}[\textit{pre}[i]-k]mp[pre[i]−k] 里记录的 \textit{pre}[j]pre[j] 的下标范围是 0\leq j\leq i0≤j≤i 。同时，由于\textit{pre}[i]pre[i] 的计算只与前一项的答案有关，因此我们可以不用建立 \textit{pre}pre 数组，直接用 \textit{pre}pre 变量来记录 pre[i-1]pre[i−1] 的答案即可。
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        mp = {0: 1} # 什么都不要，就是和为0，算是前缀和为0的一种情况
        s = 0 # sum
        n = len(nums)
        count = 0

        for i in range(n):
            s += nums[i]

            if s - k in mp:
                count += mp[s - k]
            
            mp[s] = mp.get(s, 0) + 1
        
        return count