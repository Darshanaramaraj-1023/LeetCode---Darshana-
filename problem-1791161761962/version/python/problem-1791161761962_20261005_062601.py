# Last updated: 10/5/2026, 6:26:01 AM
1class Solution:
2    def isValidSudoku(self, board):
3        
4        # Check rows
5        for i in range(9):
6            seen = set()
7
8            for j in range(9):
9                value = board[i][j]
10
11                if value == '.':
12                    continue
13
14                if value in seen:
15                    return False
16
17                seen.add(value)
18
19        # Check columns
20        for j in range(9):
21            seen = set()
22
23            for i in range(9):
24                value = board[i][j]
25
26                if value == '.':
27                    continue
28
29                if value in seen:
30                    return False
31
32                seen.add(value)
33
34        # Check 3 x 3 boxes
35        for row in range(0, 9, 3):
36            for col in range(0, 9, 3):
37
38                seen = set()
39
40                for i in range(row, row + 3):
41                    for j in range(col, col + 3):
42
43                        value = board[i][j]
44
45                        if value == '.':
46                            continue
47
48                        if value in seen:
49                            return False
50
51                        seen.add(value)
52
53        return True