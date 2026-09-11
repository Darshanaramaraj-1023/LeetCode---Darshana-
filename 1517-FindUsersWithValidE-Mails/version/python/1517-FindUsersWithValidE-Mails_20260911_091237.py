# Last updated: 9/11/2026, 9:12:37 AM
1class Solution:
2    def hasAlternatingBits(self, n):
3        
4        prev = n % 2
5        n = n // 2
6
7        while n > 0:
8            current = n % 2
9
10            if current == prev:
11                return False
12
13            prev = current
14            n = n // 2
15
16        return True