# Last updated: 8/11/2026, 4:02:44 PM
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count += 1

        return count