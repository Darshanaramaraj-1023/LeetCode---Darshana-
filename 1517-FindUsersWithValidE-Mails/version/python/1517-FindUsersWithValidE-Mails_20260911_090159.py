# Last updated: 9/11/2026, 9:01:59 AM
1class Solution:
2    def largestRectangleArea(self, heights):
3        stack = []
4        max_area = 0
5
6        heights.append(0)
7
8        for i in range(len(heights)):
9
10            while stack and heights[i] < heights[stack[-1]]:
11
12                height = heights[stack.pop()]
13
14                if stack:
15                    width = i - stack[-1] - 1
16                else:
17                    width = i
18
19                area = height * width
20                max_area = max(max_area, area)
21
22            stack.append(i)
23
24        return max_area