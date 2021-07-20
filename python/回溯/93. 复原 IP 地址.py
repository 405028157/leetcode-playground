class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        res = []

        def dfs(combination, start):
            if start >= n:
                # 恰好用完字符串组成四段ip
                if start == n and len(combination) == 4:
                    res.append('.'.join(combination))
                return

            # 有了四段ip，但是没有用完字符串，说明是无效的组合
            if len(combination) == 4 and start < n - 1:
                return

            # i = [1,3]
            for i in range(1, 4):
                temp = s[start: start + i]
                # # 切片超出范围，temp为空
                # if not temp:
                #     print(start, i, n)
                #     break
                if int(temp) > 255:
                    break
                if len(temp) > 1 and temp[0] == '0':
                    break

                dfs(combination + [temp], start + i)
        
        
        dfs([], 0)
        return res