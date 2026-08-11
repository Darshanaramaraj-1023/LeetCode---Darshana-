# Last updated: 8/11/2026, 4:02:25 PM
from math import comb
class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD=10**9+7
        if k>n:
            return 0
        total = comb(n-1,k-1)
        odd=0
        if(n-k)%2==0:
            m=(n-k)//2
            odd=comb(m+k-1,k-1)
        return(total-odd)%MOD
        