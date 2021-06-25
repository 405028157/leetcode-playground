class Union:
    def __init__(self, grid: list[list[str]]):
        m, n = len(grid), len(grid[0])
        self.rank = [0] * (m * n)
        self.parent = [0] * (m * n)
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, target):
        if self.parent[target] != target:
            return self.find(self.parent[target])
        return self.parent[target]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        # rootx 和 rooty相等就什么都不用做
        # 如果 rootx 和 rooty 不相等
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = self.parent[rootx]

            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            # 每合并一次，就减少一个整体独立的岛屿
            self.count -= 1

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        uf = Union(grid)
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)

        return uf.count
                            

s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
s.numIslands(grid)











