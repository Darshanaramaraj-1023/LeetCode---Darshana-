# Last updated: 8/11/2026, 4:02:43 PM
from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        # Find maximum value in each column
        col_max = [0] * cols

        for j in range(cols):
            maximum = 0
            for i in range(rows):
                maximum = max(maximum, matrix[i][j])
            col_max[j] = maximum

        # Replace -1 with the column maximum
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]

        return matrix