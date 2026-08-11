# Last updated: 8/11/2026, 4:01:59 PM
from math import gcd
from typing import List
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                g=gcd(nums[i],nums[j])
                strength=(nums[i]*nums[j])//(g*g)
                ans=max(ans,strength)
        return ans
        