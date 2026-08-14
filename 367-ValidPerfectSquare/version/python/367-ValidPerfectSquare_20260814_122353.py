# Last updated: 8/14/2026, 12:23:53 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        left = 0
4        right = len(nums) - 1
5
6        result = [0] * len(nums)
7        index = len(nums) - 1
8
9        while left <= right:
10            if abs(nums[left]) > abs(nums[right]):
11                result[index] = nums[left] * nums[left]
12                left += 1
13            else:
14                result[index] = nums[right] * nums[right]
15                right -= 1
16
17            index -= 1
18
19        return result