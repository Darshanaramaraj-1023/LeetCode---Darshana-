# Last updated: 8/22/2026, 9:38:15 AM
1class Solution:
2    def longestValidParentheses(self, s):
3        stack = [-1]
4        max_length = 0
5
6        for i in range(len(s)):
7
8            if s[i] == '(':
9                stack.append(i)
10
11            else:
12                stack.pop()
13
14                if not stack:
15                    # Current ')' cannot be matched
16                    stack.append(i)
17                else:
18                    # Valid substring length
19                    max_length = max(max_length, i - stack[-1])
20
21        return max_length