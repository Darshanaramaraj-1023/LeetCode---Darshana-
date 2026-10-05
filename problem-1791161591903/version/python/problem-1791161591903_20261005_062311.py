# Last updated: 10/5/2026, 6:23:11 AM
1class Solution:
2    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
3        MOD = 10**9 + 7
4
5        # Calculate final positions
6        positions = []
7
8        for i in range(len(nums)):
9            if s[i] == 'L':
10                positions.append(nums[i] - d)
11            else:
12                positions.append(nums[i] + d)
13
14        # Sort final positions
15        positions.sort()
16
17        # Calculate sum of pairwise distances
18        ans = 0
19        prefix = 0
20
21        for i in range(len(positions)):
22            ans += positions[i] * i - prefix
23            prefix += positions[i]
24
25        return ans % MOD