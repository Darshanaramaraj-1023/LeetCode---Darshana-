# Last updated: 9/15/2026, 3:47:49 PM
1class Solution:
2    def maxSubarraySumCircular(self, nums):
3
4        total = sum(nums)
5
6        # Kadane's algorithm for maximum subarray
7        current_max = 0
8        max_sum = nums[0]
9
10        # Kadane's algorithm for minimum subarray
11        current_min = 0
12        min_sum = nums[0]
13
14        for x in nums:
15
16            # Maximum subarray
17            current_max = max(x, current_max + x)
18            max_sum = max(max_sum, current_max)
19
20            # Minimum subarray
21            current_min = min(x, current_min + x)
22            min_sum = min(min_sum, current_min)
23
24        # All numbers are negative
25        if max_sum < 0:
26            return max_sum
27
28        # Circular case
29        circular_sum = total - min_sum
30
31        return max(max_sum, circular_sum)