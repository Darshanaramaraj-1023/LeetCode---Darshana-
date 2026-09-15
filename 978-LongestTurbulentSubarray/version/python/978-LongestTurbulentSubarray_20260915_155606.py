# Last updated: 9/15/2026, 3:56:06 PM
1class Solution:
2    def subarraySum(self, nums, k):
3        prefix_sum = 0
4        count = 0
5
6        # prefix_sum : frequency
7        seen = {0: 1}
8
9        for num in nums:
10            prefix_sum += num
11
12            # Check whether a previous prefix gives sum k
13            needed = prefix_sum - k
14
15            if needed in seen:
16                count += seen[needed]
17
18            # Store current prefix sum
19            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
20
21        return count