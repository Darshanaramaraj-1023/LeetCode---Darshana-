# Last updated: 8/11/2026, 4:02:12 PM
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        if s>9*n:
            return -1
        digits=[]
        for _ in range(n):
            d=min(9,s)
            digits.append(str(d))
            s-=d
        return int("".join(digits))