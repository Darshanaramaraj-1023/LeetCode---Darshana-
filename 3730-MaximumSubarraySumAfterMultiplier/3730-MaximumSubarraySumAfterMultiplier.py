# Last updated: 8/11/2026, 4:02:33 PM
class Solution:
    def maxSubarraySum(self, nums, k):
        NEG=float("-inf")
        def transform(x,multiply):
            if multiply:
                return x*k
            if x>=0:
                return x//k
            return-((-x)//k)
        def solve(multiply):
            dp0=nums[0]
            dp1=transform(nums[0],multiply)
            dp2=NEG
            ans = max(dp0, dp1)
            for i in range(1,len(nums)):
                a=nums[i]
                b=transform(a,multiply)

                ndp0=max(dp0+a,a)
                ndp1=max(dp1+b,dp0+b,b)
                ndp2=max(dp2+a,dp1+a)

                dp0,dp1,dp2=ndp0,ndp1,ndp2
                ans=max(ans,dp0,dp1,dp2)
            return ans
        return max(solve(True),solve(False))
        