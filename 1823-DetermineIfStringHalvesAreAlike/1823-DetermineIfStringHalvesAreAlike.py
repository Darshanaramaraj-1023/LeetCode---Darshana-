# Last updated: 8/11/2026, 4:04:30 PM
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s)
        count1 = 0
        count2 = 0

        for i in range(n // 2):
            if s[i] in vowels:
                count1 += 1

        for i in range(n // 2, n):
            if s[i] in vowels:
                count2 += 1

        return count1 == count2