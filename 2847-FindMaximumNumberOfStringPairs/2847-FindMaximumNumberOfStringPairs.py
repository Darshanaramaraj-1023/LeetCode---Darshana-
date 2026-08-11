# Last updated: 8/11/2026, 4:03:14 PM
class Solution:
    def maximumNumberOfStringPairs(self, words):
        seen = set()
        count = 0

        for word in words:
            rev = word[::-1]

            if rev in seen:
                count += 1
            else:
                seen.add(word)

        return count