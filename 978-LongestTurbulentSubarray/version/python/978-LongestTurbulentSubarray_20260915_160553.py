# Last updated: 9/15/2026, 4:05:53 PM
1class Solution:
2    def reverseWords(self, s):
3        words = s.split()
4
5        words.reverse()
6
7        return " ".join(words)