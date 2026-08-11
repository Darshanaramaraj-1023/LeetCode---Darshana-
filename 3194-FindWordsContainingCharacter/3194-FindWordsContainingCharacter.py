# Last updated: 8/11/2026, 4:03:03 PM
class Solution:
    def findWordsContaining(self, words, x):
        ans = []

        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)

        return ans