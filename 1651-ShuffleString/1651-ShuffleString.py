# Last updated: 8/11/2026, 4:04:45 PM
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)

        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return "".join(ans)