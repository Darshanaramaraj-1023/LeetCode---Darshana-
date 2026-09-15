# Last updated: 9/15/2026, 3:59:23 PM
1class Solution:
2    def merge(self, intervals):
3        intervals.sort()
4
5        result = []
6
7        for interval in intervals:
8            start = interval[0]
9            end = interval[1]
10
11            # No overlap
12            if not result or start > result[-1][1]:
13                result.append([start, end])
14
15            # Overlap
16            else:
17                result[-1][1] = max(result[-1][1], end)
18
19        return result