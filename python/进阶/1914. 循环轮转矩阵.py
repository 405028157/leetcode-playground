class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(int(m / 2), int(n / 2))
        # print(f'm = {m}, n = {n}')
        for layer in range(nlayer):
            print(layer)
            row, col, val = [], [], []

            # 左
            for r in range(layer, m - layer - 1):
                row.append(r)
                col.append(layer)
                # print(f'r = {r}, layer = {layer}')
                val.append(grid[r][layer])
            
            # 下
            for c in range(layer, n - layer - 1):
                row.append(m - 1 - layer)
                col.append(c)
                val.append(grid[m - 1 - layer][c])
            
            # 右
            for r in range(m - 1 - layer, layer, -1):
                row.append(r)
                col.append(n - 1 - layer)
                val.append(grid[r][n - 1 - layer])
            
            # 上
            for c in range(n - 1 - layer, layer, -1):
                row.append(layer)
                col.append(c)
                val.append(grid[layer][c])
            
            total = len(val)
            kk = k % total

            for i in range(total):
                # (i - kk) 可能为负值，而 kk 一定小于 total，所以加上total，再对total取余，可以保证是正值
                index = (i + total - kk) % total
                grid[row[i]][col[i]] = val[index]
        
        return grid
            