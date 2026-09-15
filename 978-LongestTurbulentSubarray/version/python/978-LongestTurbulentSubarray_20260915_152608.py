# Last updated: 9/15/2026, 3:26:08 PM
1class Solution:
2    def maximumSetSize(self, nums1, nums2):
3        n = len(nums1)
4        half = n // 2
5
6        set1 = set(nums1)
7        set2 = set(nums2)
8
9        all_values = set1 | set2
10
11        return min(
12            n,
13            half + len(set1),
14            half + len(set2),
15            len(all_values)
16        )