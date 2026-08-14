# Last updated: 8/14/2026, 12:22:16 PM
1class Solution:
2    def peakIndexInMountainArray(self, arr: List[int]) -> int:
3        left = 0
4        right = len(arr) - 1
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if arr[mid] < arr[mid + 1]:
10                # We are on the increasing side
11                left = mid + 1
12            else:
13                # We are on the decreasing side
14                right = mid
15
16        return left