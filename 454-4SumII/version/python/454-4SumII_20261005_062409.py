# Last updated: 10/5/2026, 6:24:09 AM
1class Solution:
2    def fourSumCount(self, nums1, nums2, nums3, nums4):
3        count = {}
4
5        # Store sums of nums1 and nums2
6        for a in nums1:
7            for b in nums2:
8                total = a + b
9                count[total] = count.get(total, 0) + 1
10
11        ans = 0
12
13        # Find opposite sums in nums3 and nums4
14        for c in nums3:
15            for d in nums4:
16                total = c + d
17
18                if -total in count:
19                    ans += count[-total]
20
21        return ans