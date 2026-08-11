# Last updated: 8/11/2026, 4:08:31 PM
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper() or
            word.islower() or
            word.istitle()
        )