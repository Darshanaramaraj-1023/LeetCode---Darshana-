# Last updated: 8/11/2026, 4:11:49 PM
class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result += chr(ord('A') + remainder)
            columnNumber //= 26

        return result[::-1]