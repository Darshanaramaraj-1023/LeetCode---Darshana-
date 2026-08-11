# Last updated: 8/11/2026, 4:09:16 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1