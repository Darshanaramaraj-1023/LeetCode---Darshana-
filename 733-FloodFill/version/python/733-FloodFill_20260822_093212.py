# Last updated: 8/22/2026, 9:32:12 AM
1class Solution:
2    def minCostClimbingStairs(self, cost):
3        n = len(cost)
4
5        dp = [0] * (n + 1)
6
7        dp[0] = 0
8        dp[1] = 0
9
10        for i in range(2, n + 1):
11            dp[i] = min(
12                dp[i - 1] + cost[i - 1],
13                dp[i - 2] + cost[i - 2]
14            )
15
16        return dp[n]