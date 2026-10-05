# Last updated: 10/5/2026, 6:21:23 AM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7        current_row = 0
8        direction = 1
9
10        for ch in s:
11            rows[current_row] += ch
12
13            if current_row == 0:
14                direction = 1
15            elif current_row == numRows - 1:
16                direction = -1
17
18            current_row += direction
19
20        return "".join(rows)