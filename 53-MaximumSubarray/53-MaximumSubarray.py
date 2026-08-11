# Last updated: 8/11/2026, 4:12:58 PM
class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum