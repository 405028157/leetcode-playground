class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        ans = 0
        

        def dfs(rest:int):
            nonlocal ans
            if rest == 0:
                ans += 1
                return

            # 题目没说整数不可以是负数，先当做不可以吧
            if rest < 0:
                return

            for num in nums:
                dfs(rest - num)
        
        dfs(target)
        return ans
            
                
