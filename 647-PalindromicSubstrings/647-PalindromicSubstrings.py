# Last updated: 8/11/2026, 4:07:31 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd-length palindrome
            expand(i, i)

            # Even-length palindrome
            expand(i, i + 1)

        return count