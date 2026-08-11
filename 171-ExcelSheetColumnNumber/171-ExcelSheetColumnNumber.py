# Last updated: 8/11/2026, 4:11:41 PM
class Solution:
    def titleToNumber(self, columnTitle):
        result = 0

        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            result = result * 26 + value

        return result