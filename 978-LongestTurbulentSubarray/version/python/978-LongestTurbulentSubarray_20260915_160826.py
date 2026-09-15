# Last updated: 9/15/2026, 4:08:26 PM
1class Solution:
2    def findMin(self, nums):
3        left = 0
4        right = len(nums) - 1
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if nums[mid] > nums[right]:
10                left = mid + 1
11
12            elif nums[mid] < nums[right]:
13                right = mid
14
15            else:
16                right -= 1
17
18        return nums[left]