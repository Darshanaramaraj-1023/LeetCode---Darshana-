# Last updated: 8/14/2026, 12:19:40 PM
1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        left = 1
4        right = num
5
6        while left <= right:
7            mid = (left + right) // 2
8            square = mid * mid
9
10            if square == num:
11                return True
12            elif square < num:
13                left = mid + 1
14            else:
15                right = mid - 1
16
17        return False