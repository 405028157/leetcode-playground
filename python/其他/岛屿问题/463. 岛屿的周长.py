"""
对于一个陆地格子的每条边，它被算作岛屿的周长当且仅当这条边为网格的边界或者相邻的另一个格子为水域。
"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])

        def calculate_length(x, y):
            # print(x, y)
            count = 0
            if x == 0 or grid[x - 1][y] == 0: count += 1
            if x == m - 1 or grid[x + 1][y] == 0: count += 1
            if y == 0 or grid[x][y - 1] == 0: count += 1
            if y == n - 1 or grid[x][y + 1] == 0: count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += calculate_length(i, j)

        return perimeter