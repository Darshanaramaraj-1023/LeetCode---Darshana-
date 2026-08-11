# Last updated: 8/11/2026, 4:08:30 PM
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        first_index = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in first_index:
                max_length = max(max_length, i - first_index[count])
            else:
                first_index[count] = i

        return max_length