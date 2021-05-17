"""
**约定： 用nums[i...j]代表 nums[i] + nums[i+1] + ... + nums[j]
**做法：滑动窗口，i, j都从头开始，j前进到让sum = nums[i...j]元素和大于target的时候，就找到了以i开头，满足条件的长度最小的序列，此时 i += 1，若nums[i+1, ..., j]仍然大于等于target，就找到了以 i+1 开头，满足条件的长度最小的序列。直到 sum < target，再重复这个过程。
**证明/理解：从俩方面证明，对每个i是否找到了最近（小）的j，和对每个j是否找到了最近（大）的i
1、对每个i，当j增加到恰好sum >= target时，就停止，所以找到的是最小的j。若i是自增之后，仍有sum < target，因为sum[i,i+1...,j-1] < target，因为数组元素为正，所以肯定有sum[i+1,...,j-1] < target,而sum[i+1,...,j]>=target，
所以对于i+1，找到也是最小的j.
2、其实只要每个i都找到了最小的j，就已经足够了。第二方面不需要证
可以看题解动画理解下https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
**注意不需要排序，因为数组元素为正，所以可以保证丢掉元素，和增加元素时候的“单调”
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        if not nums:
            return 0
        i, j = 0, 0 # 窗口的左和右“指针”
        n = len(nums)
        ans = n + 1 # 先取一个很大的数，比数组长度大就足够了
        sum = 0
        while j < n:
            sum += nums[j]
            while sum >= target:
                ans = min(ans, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        return ans