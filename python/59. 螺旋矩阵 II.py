"""
这是一个状态机，代表前进的方向转换：右 -> 下， 下 -> 左, 左 -> 上, 上 -> 右
右: {1, 0}, 下: {0, 1}, 左: {-1, 0}, 上: {0, -1}, 建一个类似的字典，来代表在某个方向走一步时，x和y的变化
"""

class Solution:
    dircState = {'right': 'bottom', 'bottom': 'left', 'left': 'top', 'top': 'right'}
    dircHash = {'right': {1, 0}, 'bottom': {0, 1}, 'left': {-1, 0}, 'top': {0, 1}}
    def needTurn(self, x, y, n, direction):
        if direction == 'right' and x == n - 1:
            return True
        if direction == 'left' and x == 0:
            return True
        if direction == 'top' and y == 0:
            return True
        if direction == 'bottom' and y == n - 1:
            return True
        return False

    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for i in range(n)]
        count = 1
        totalCount = n ** 2
        curState = 'right'
        x, y = 0, 0
        while count <= totalCount:
            print(f'x = {x}, y = {y}, curStat = {curState}, self.dircHash[curState] = {self.dircHash[curState]}')
            # 这里先赋值，需要理解下，因为即使当前的x, y需要转弯了，但是matrix[x][y]依然是合法的，并且在循环之前没有给matrix赋过值
            matrix[x][y] = count
            count += 1
            if self.needTurn(x, y, n, curState):
                curState = self.dircState[curState]
            x_dirc, y_dirc = self.dircHash[curState]
            x += x_dirc
            y += y_dirc
        return matrix

s = Solution()
# s.generateMatrix(3)
print(s.dircHash['right'])
    
   