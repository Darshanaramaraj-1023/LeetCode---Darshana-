# Last updated: 9/15/2026, 3:51:06 PM
1class Solution:
2    def productExceptSelf(self, nums):
3        n = len(nums)
4
5        answer = [1] * n
6
7        # Left products
8        left = 1
9
10        for i in range(n):
11            answer[i] = left
12            left *= nums[i]
13
14        # Right products
15        right = 1
16
17        for i in range(n - 1, -1, -1):
18            answer[i] *= right
19            right *= nums[i]
20
21        return answer