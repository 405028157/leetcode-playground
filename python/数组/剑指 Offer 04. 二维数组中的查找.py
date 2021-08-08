class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        
        i, j = 0, col - 1

        while i < row and j >= 0 and matrix[i][j] != target:
            if matrix[i][j] == target:
                break
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        if i >= row or j < 0:
            return False
        
        return True
            