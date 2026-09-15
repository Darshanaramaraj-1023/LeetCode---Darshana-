# Last updated: 9/15/2026, 3:31:47 PM
1class Solution:
2    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
3
4        # Check if rook can capture queen
5        if a == e:
6            # Bishop blocks the rook horizontally
7            if not (c == a and min(b, f) < d < max(b, f)):
8                return 1
9
10        if b == f:
11            # Bishop blocks the rook vertically
12            if not (d == b and min(a, e) < c < max(a, e)):
13                return 1
14
15        # Check if bishop can capture queen
16        if abs(c - e) == abs(d - f):
17
18            # Rook blocks the bishop
19            if abs(a - c) == abs(b - d) and \
20               abs(a - e) == abs(b - f) and \
21               min(c, e) < a < max(c, e):
22                return 2
23
24            return 1
25
26        return 2