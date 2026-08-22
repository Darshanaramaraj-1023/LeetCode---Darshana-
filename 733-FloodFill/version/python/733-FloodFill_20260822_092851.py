# Last updated: 8/22/2026, 9:28:51 AM
1class Solution:
2    def findContentChildren(self, g, s):
3        g.sort()
4        s.sort()
5
6        child = 0
7        cookie = 0
8
9        while child < len(g) and cookie < len(s):
10
11            if s[cookie] >= g[child]:
12                # Cookie satisfies the child
13                child += 1
14
15            # Move to the next cookie
16            cookie += 1
17
18        return child