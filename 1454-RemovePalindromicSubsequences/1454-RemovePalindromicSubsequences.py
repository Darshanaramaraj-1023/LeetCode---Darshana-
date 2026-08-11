# Last updated: 8/11/2026, 4:05:00 PM
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2