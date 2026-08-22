# Last updated: 8/22/2026, 9:24:10 AM
1class Solution:
2    def floodFill(self, image, sr, sc, color):
3        original = image[sr][sc]
4
5        # If the color is already the same, no changes needed
6        if original == color:
7            return image
8
9        def dfs(r, c):
10            # Check boundaries
11            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
12                return
13
14            # Only fill pixels with the original color
15            if image[r][c] != original:
16                return
17
18            # Change the color
19            image[r][c] = color
20
21            # Visit 4 directions
22            dfs(r - 1, c)  # Up
23            dfs(r + 1, c)  # Down
24            dfs(r, c - 1)  # Left
25            dfs(r, c + 1)  # Right
26
27        dfs(sr, sc)
28
29        return image