# Last updated: 8/11/2026, 4:09:12 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s:
            result ^= ord(ch)

        for ch in t:
            result ^= ord(ch)

        return chr(result)