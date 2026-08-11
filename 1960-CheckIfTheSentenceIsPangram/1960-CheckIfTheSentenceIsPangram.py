# Last updated: 8/11/2026, 4:04:16 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26