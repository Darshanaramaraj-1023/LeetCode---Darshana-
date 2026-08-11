# Last updated: 8/11/2026, 4:03:01 PM
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)

        for i in range(len(nums) - 1, 1, -1):
            if total - nums[i] > nums[i]:
                return total
            total -= nums[i]

        return -1