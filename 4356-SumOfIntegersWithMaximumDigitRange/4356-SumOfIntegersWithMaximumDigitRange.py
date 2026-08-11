# Last updated: 8/11/2026, 4:02:10 PM
class Solution:
    def maxDigitRange(self, nums):
        max_range =-1
        ans = 0
        for num in nums:
            digits=[int(d) for d in str(num)]
            digit_range=max(digits)-min(digits)
            if digit_range > max_range:
                max_range=digit_range
                ans=num
            elif digit_range==max_range:
                ans+=num
        return ans
        