# Last updated: 8/22/2026, 9:45:43 AM
1class Solution:
2    def find132pattern(self, nums):
3        stack = []
4        second = float('-inf')
5
6        # Scan from right to left
7        for i in range(len(nums) - 1, -1, -1):
8
9            # nums[i] is the "1"
10            if nums[i] < second:
11                return True
12
13            # Find the largest possible "2"
14            while stack and nums[i] > stack[-1]:
15                second = stack.pop()
16
17            # nums[i] becomes a possible "3"
18            stack.append(nums[i])
19
20        return False