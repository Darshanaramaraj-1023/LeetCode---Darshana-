# Last updated: 9/15/2026, 3:40:42 PM
1class Solution:
2    def reverseStr(self, s, k):
3        s = list(s)
4
5        for i in range(0, len(s), 2 * k):
6            s[i:i + k] = reversed(s[i:i + k])
7
8        return ''.join(s)