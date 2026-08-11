# Last updated: 8/11/2026, 4:04:14 PM
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""] * len(words)

        for word in words:
            pos = int(word[-1]) - 1
            result[pos] = word[:-1]

        return " ".join(result)