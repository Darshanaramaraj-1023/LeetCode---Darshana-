# Last updated: 8/11/2026, 4:02:49 PM
class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        for i in range(len(word)):
            ans += i // 8 + 1

        return ans