# Last updated: 8/11/2026, 4:04:12 PM
from collections import Counter

class Solution:
    def makeEqual(self, words):
        count = Counter()

        for word in words:
            count.update(word)

        n = len(words)

        for freq in count.values():
            if freq % n != 0:
                return False

        return True