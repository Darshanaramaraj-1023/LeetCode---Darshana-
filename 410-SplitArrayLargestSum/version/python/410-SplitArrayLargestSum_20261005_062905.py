# Last updated: 10/5/2026, 6:29:05 AM
1class Solution:
2    def splitArray(self, nums, k):
3        left = max(nums)
4        right = sum(nums)
5
6        while left < right:
7            mid = (left + right) // 2
8
9            subarrays = 1
10            current_sum = 0
11
12            for num in nums:
13                if current_sum + num > mid:
14                    subarrays += 1
15                    current_sum = num
16                else:
17                    current_sum += num
18
19            if subarrays <= k:
20                right = mid
21            else:
22                left = mid + 1
23
24        return left