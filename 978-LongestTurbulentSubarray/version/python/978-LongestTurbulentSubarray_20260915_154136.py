# Last updated: 9/15/2026, 3:41:36 PM
1class Solution:
2    def spiralOrder(self, matrix):
3        result = []
4
5        top = 0
6        bottom = len(matrix) - 1
7        left = 0
8        right = len(matrix[0]) - 1
9
10        while top <= bottom and left <= right:
11
12            # 1. Move from left to right
13            for i in range(left, right + 1):
14                result.append(matrix[top][i])
15
16            top += 1
17
18            # 2. Move from top to bottom
19            for i in range(top, bottom + 1):
20                result.append(matrix[i][right])
21
22            right -= 1
23
24            # 3. Move from right to left
25            if top <= bottom:
26                for i in range(right, left - 1, -1):
27                    result.append(matrix[bottom][i])
28
29                bottom -= 1
30
31            # 4. Move from bottom to top
32            if left <= right:
33                for i in range(bottom, top - 1, -1):
34                    result.append(matrix[i][left])
35
36                left += 1
37
38        return result