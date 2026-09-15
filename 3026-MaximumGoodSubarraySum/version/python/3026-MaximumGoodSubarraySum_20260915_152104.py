# Last updated: 9/15/2026, 3:21:04 PM
1class Solution:
2    def maximumSubarraySum(self, nums, k):
3        prefix = 0
4        best = {}
5        ans = float('-inf')
6
7        for x in nums:
8            # Prefix sum before current element
9            old_prefix = prefix
10
11            # Add current element
12            prefix += x
13
14            # Current x needs starting value x-k or x+k
15            if x - k in best:
16                ans = max(ans, prefix - best[x - k])
17
18            if x + k in best:
19                ans = max(ans, prefix - best[x + k])
20
21            # Store the smallest prefix sum before x
22            if x not in best:
23                best[x] = old_prefix
24            else:
25                best[x] = min(best[x], old_prefix)
26
27        return 0 if ans == float('-inf') else ans