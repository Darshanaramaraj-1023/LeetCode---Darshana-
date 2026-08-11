# Last updated: 8/11/2026, 4:06:43 PM
class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        result = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            result.append(row)
        return result