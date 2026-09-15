# Last updated: 9/15/2026, 3:23:59 PM
1class Solution:
2    def maxTurbulenceSize(self, arr):
3        n = len(arr)
4
5        if n == 1:
6            return 1
7
8        ans = 1
9        left = 0
10
11        for i in range(1, n):
12            if arr[i] == arr[i - 1]:
13                left = i
14
15            elif i == 1 or (
16                (arr[i] > arr[i - 1]) !=
17                (arr[i - 1] > arr[i - 2])
18            ):
19                pass
20
21            else:
22                left = i - 1
23
24            ans = max(ans, i - left + 1)
25
26        return ans