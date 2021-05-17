"""
这是一个状态机，代表前进的方向转换：右 -> 下， 下 -> 左, 左 -> 上, 上 -> 右
右: {1, 0}, 下: {0, 1}, 左: {-1, 0}, 上: {0, -1}, 建一个类似的字典，来代表在某个方向走一步时，x和y的变化
"""

class Solution:
    dircState = {'right': 'bottom', 'bottom': 'left', 'left': 'top', 'top': 'right'}
    dircHash = {'right': [0, 1], 'bottom': [1, 0], 'left': [0, -1], 'top': [-1, 0]}
    def needTurn(self, x, y, n, direction, matrix):
        x_dirc, y_dirc = self.dircHash[direction]
        x_after, y_after = x + x_dirc, y + y_dirc
        if x_after < 0 or x_after >= n:
            return True
        if y_after < 0 or y_after >= n:
            return True
        if matrix[x_after][y_after] != 0: #已经填过了，需要提前拐
            return True
        return False

    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for i in range(n)]
        count = 1
        totalCount = n ** 2
        curState = 'right'
        # x 代表行，y代表列
        x, y = 0, 0
        while count <= totalCount:
            print(f'x = {x}, y = {y}, count = {count} curStat = {curState}, self.dircHash[curState] = {self.dircHash[curState]} ', end = '')
            # 这里先赋值，需要理解下，因为即使当前的x, y需要转弯了，但是matrix[x][y]依然是合法的，并且在循环之前没有给matrix赋过值
            matrix[x][y] = count
            count += 1
            if self.needTurn(x, y, n, curState, matrix):
                curState = self.dircState[curState]
            print(f'nextStat = {curState} ', end = '')
            x_dirc, y_dirc = self.dircHash[curState]
            print(f'x_dirc = {x_dirc}, y_dirc = {y_dirc}')
            x += x_dirc
            y += y_dirc
        return matrix

s = Solution()
m = s.generateMatrix(3)
print(m)
# print(s.dircHash['right'])
    
   