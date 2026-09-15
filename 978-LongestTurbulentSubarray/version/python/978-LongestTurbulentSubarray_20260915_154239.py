# Last updated: 9/15/2026, 3:42:39 PM
1class Solution:
2    def generateMatrix(self, n):
3        matrix = [[0] * n for _ in range(n)]
4
5        top = 0
6        bottom = n - 1
7        left = 0
8        right = n - 1
9
10        num = 1
11
12        while top <= bottom and left <= right:
13
14            # 1. Left → Right
15            for col in range(left, right + 1):
16                matrix[top][col] = num
17                num += 1
18
19            top += 1
20
21            # 2. Top → Bottom
22            for row in range(top, bottom + 1):
23                matrix[row][right] = num
24                num += 1
25
26            right -= 1
27
28            # 3. Right → Left
29            if top <= bottom:
30                for col in range(right, left - 1, -1):
31                    matrix[bottom][col] = num
32                    num += 1
33
34                bottom -= 1
35
36            # 4. Bottom → Top
37            if left <= right:
38                for row in range(bottom, top - 1, -1):
39                    matrix[row][left] = num
40                    num += 1
41
42                left += 1
43
44        return matrix