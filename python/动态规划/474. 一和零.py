"""
dp[i][j][k]表示使用str前i个元素，m = j, n = k时，最大子集大小
dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - strs[i]的0数量][k - strs[i]的1数量] + 1)
"""

import collections

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dic = collections.Counter()
        for s in strs:
            dic[s] = (s.count('0'), s.count('1'))
        
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for __ in range(length + 1)]
        
        # i = 0, 或 j = 0 且 k = 0 时，对应的所有元素都是0，所以初始化省了
        for i in range(1, length + 1):
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    count = dic[strs[i - 1]]
                    count_0 = count[0]
                    count_1 = count[1]
                    # print(count)
                    
                    if count_0 <= j and count_1 <= k:
                        # print(f'i = {i}, j = {j}, k = {k}, dp[i][j][k] = {dp[i][j][k]}, dp[i - 1][j - count_0][k - count_1] = {dp[i - 1][j - count_0][k - count_1]}')
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - count_0][k - count_1] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        # dp[3][1][1] = dp[2][0][1] + 1 = dp[1][0][0] + 1
        # print(dp[2][0][1])
        return dp[length][m][n]