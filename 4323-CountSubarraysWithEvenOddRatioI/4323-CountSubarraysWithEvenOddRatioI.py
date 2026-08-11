# Last updated: 8/11/2026, 4:02:30 PM
from typing import List
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            even=0
            odd=0
            for j in range(i,n):
                if nums[j]%2==0:
                    even+=1
                else:
                    odd+=1
                if odd>0 and even*b<=odd*a:
                    ans+=1
        return ans
        