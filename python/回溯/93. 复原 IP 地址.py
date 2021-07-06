class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        res = []

        def dfs(combination, start):
            # 用完了所有字符串，但是没有组成四段ip
            if start >= n and len(combination) < 4:
                return

            # 有了四段ip，但是没有用完字符串，说明是无效的组合
            if len(combination) == 4 and start < n - 1:
                return
            
            # 恰好用完字符串组成四段ip
            if len(combination) == 4 and start == n:
                res.append('.'.join(combination))

            for i in range(3):
                temp = s[start: start + i]
                print(temp)
                if int(temp) > 255:
                    break
                if len(temp) > 1 and temp[0] == '0':
                    break

                dfs(combination.append(temp), start + i)
        
        
        dfs([], 0)
        return res