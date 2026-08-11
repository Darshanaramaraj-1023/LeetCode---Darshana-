# Last updated: 8/11/2026, 4:02:13 PM
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD=10**9+7
        resource = k
        operations=0
        cost=0
        for x in nums:
            if resource<x:
                need = x-resource
                t=(need+k-1)//k
                cost=(cost+t*(2*operations+t+1)//2)%MOD
                operations+=t
                resource+=t*k
            resource-=x
        return cost
        