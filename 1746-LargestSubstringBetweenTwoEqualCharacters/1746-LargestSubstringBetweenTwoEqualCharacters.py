# Last updated: 8/11/2026, 4:04:42 PM
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            else:
                ans = max(ans, i - first[ch] - 1)

        return ans