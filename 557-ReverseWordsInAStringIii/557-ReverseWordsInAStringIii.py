# Last updated: 8/11/2026, 4:08:26 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []

        for word in words:
            result.append(word[::-1])

        return " ".join(result)