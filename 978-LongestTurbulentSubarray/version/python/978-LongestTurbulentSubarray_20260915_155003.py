# Last updated: 9/15/2026, 3:50:03 PM
1class Solution:
2    def longestConsecutive(self, nums):
3        num_set = set(nums)
4        longest = 0
5
6        for num in num_set:
7
8            # Start only if num is the beginning
9            if num - 1 not in num_set:
10
11                current = num
12                length = 1
13
14                # Find consecutive numbers
15                while current + 1 in num_set:
16                    current += 1
17                    length += 1
18
19                longest = max(longest, length)
20
21        return longest