# Last updated: 8/22/2026, 9:26:10 AM
1class Solution:
2    def islandPerimeter(self, grid):
3        rows = len(grid)
4        cols = len(grid[0])
5        perimeter = 0
6
7        for r in range(rows):
8            for c in range(cols):
9
10                if grid[r][c] == 1:
11
12                    # Up
13                    if r == 0 or grid[r - 1][c] == 0:
14                        perimeter += 1
15
16                    # Down
17                    if r == rows - 1 or grid[r + 1][c] == 0:
18                        perimeter += 1
19
20                    # Left
21                    if c == 0 or grid[r][c - 1] == 0:
22                        perimeter += 1
23
24                    # Right
25                    if c == cols - 1 or grid[r][c + 1] == 0:
26                        perimeter += 1
27
28        return perimeter