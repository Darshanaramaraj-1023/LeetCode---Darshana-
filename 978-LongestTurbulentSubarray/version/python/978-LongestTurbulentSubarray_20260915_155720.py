# Last updated: 9/15/2026, 3:57:20 PM
1class Solution:
2    def maxProduct(self, nums):
3        max_product = nums[0]
4        min_product = nums[0]
5        answer = nums[0]
6
7        for i in range(1, len(nums)):
8            num = nums[i]
9
10            current_max = max(
11                num,
12                num * max_product,
13                num * min_product
14            )
15
16            current_min = min(
17                num,
18                num * max_product,
19                num * min_product
20            )
21
22            max_product = current_max
23            min_product = current_min
24
25            answer = max(answer, max_product)
26
27        return answer