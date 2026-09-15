# Last updated: 9/15/2026, 4:02:42 PM
1class Solution:
2    def longestPalindrome(self, s):
3        start = 0
4        end = 0
5
6        for i in range(len(s)):
7
8            # Odd-length palindrome
9            left = i
10            right = i
11
12            while left >= 0 and right < len(s) and s[left] == s[right]:
13                if right - left > end - start:
14                    start = left
15                    end = right
16
17                left -= 1
18                right += 1
19
20            # Even-length palindrome
21            left = i
22            right = i + 1
23
24            while left >= 0 and right < len(s) and s[left] == s[right]:
25                if right - left > end - start:
26                    start = left
27                    end = right
28
29                left -= 1
30                right += 1
31
32        return s[start:end + 1]