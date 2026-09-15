# Last updated: 9/15/2026, 4:07:13 PM
1class Solution:
2    def minSteps(self, s, t):
3        count_s = [0] * 26
4        count_t = [0] * 26
5
6        for ch in s:
7            count_s[ord(ch) - ord('a')] += 1
8
9        for ch in t:
10            count_t[ord(ch) - ord('a')] += 1
11
12        steps = 0
13
14        for i in range(26):
15            if count_t[i] > count_s[i]:
16                steps += count_t[i] - count_s[i]
17
18        return steps