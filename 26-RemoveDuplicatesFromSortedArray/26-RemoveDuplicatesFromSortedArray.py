# Last updated: 8/11/2026, 4:13:29 PM
class Solution:
    def removeDuplicates(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1