class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # [1, 1, 1, 3] 这种只能用set来去重
        # s = set()
        ans = []
        path = []
        candidates.sort()
        n = len(candidates)
        print(f'candidates = {candidates}')
        def dfs(cur: int, sum: int):
            print(f'cur = {cur}, path = {path}, sum = {sum}')
            if sum == 0:
                ans.append(path[:])
                return
            
            if cur >= n:
                return

            if sum < 0:
                return
            # 遇到了连续相同的值单独处理下
            if cur < n - 1 and candidates[cur] == candidates[cur + 1]:
                index = cur + 1
                while candidates[index] == candidates[cur]:
                    index += 1
                # 下标[cur, cur + 1, ..., index - 1]的值相同
                
                # 一共 index - cur 个相同的值，可以选[0, index - cur]个该值
                dfs(index, sum)
                print(f'一共 index - cur 个相同的值，可以选[0, index - cur]个该值, index - cur = {index - cur}')
                for i in range(1, index - cur + 1):
                    path.append(candidates[cur])
                    dfs(index, sum - candidates[cur] * i)
                
                return
            
            # 不是连续相同的值，正常处理
            path.append(candidates[cur])
            dfs(cur + 1, sum - candidates[cur])
            path.pop()
            dfs(cur + 1, sum)
        
        dfs(0, target)

        return ans

"""
candidates = [1, 2, 2, 2, 5]
cur = 0, path = [], sum = 5
	cur = 1, path = [1], sum = 4
		cur = 4, path = [1], sum = 4
			cur = 5, path = [1, 5], sum = -1
			cur = 5, path = [1], sum = 4
一共 index - cur 个相同的值，可以选[0, index - cur]个该值, index -  cur = 3
		cur = 4, path = [1, 2], sum = 2
			cur = 5, path = [1, 2, 5], sum = -3
			cur = 5, path = [1, 2], sum = 2
		cur = 4, path = [1, 2, 2], sum = 0
		cur = 4, path = [1, 2, 2, 2], sum = -2
	cur = 1, path = [1, 2, 2], sum = 5
cur = 4, path = [1, 2, 2], sum = 5
cur = 5, path = [1, 2, 2, 5], sum = 0
cur = 5, path = [1, 2, 2], sum = 5
一共 index - cur 个相同的值，可以选[0, index - cur]个该值, index -  cur = 3
cur = 4, path = [1, 2, 2, 2], sum = 3
cur = 5, path = [1, 2, 2, 2, 5], sum = -2
cur = 5, path = [1, 2, 2, 2], sum = 3
cur = 4, path = [1, 2, 2, 2, 2], sum = 1
cur = 5, path = [1, 2, 2, 2, 2, 5], sum = -4
cur = 5, path = [1, 2, 2, 2, 2], sum = 1
cur = 4, path = [1, 2, 2, 2, 2, 2], sum = -1
"""