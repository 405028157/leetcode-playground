"""
二叉搜索树的中序遍历肯定是递增的，所以中序遍历唯一，由于中序遍历结合前序遍历就可以唯一确定一个二叉树，所以问题转化为前序遍历的个数【不好实现】
中序遍历[1,2,3,...,n], root可以是任何一个，然后可以分解成n个更小的问题
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # i = [2, n]  j = [1, i]
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # print(f'i = {i}, j = {j}')
                dp[i] += dp[j - 1] * dp[i - j]
                # print(dp[i])
        
        return dp[n]
