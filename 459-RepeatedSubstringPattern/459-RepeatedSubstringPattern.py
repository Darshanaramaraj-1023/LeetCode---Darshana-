# Last updated: 8/11/2026, 4:08:46 PM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]