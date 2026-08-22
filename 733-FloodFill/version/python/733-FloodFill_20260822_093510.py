# Last updated: 8/22/2026, 9:35:10 AM
1class Solution:
2    def countBits(self, n):
3        ans = [0] * (n + 1)
4
5        for i in range(1, n + 1):
6            ans[i] = ans[i >> 1] + (i & 1)
7
8        return ans