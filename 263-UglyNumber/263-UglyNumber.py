# Last updated: 8/11/2026, 4:09:57 PM
class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1