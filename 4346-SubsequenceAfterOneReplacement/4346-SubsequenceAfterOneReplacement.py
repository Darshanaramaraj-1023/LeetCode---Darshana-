# Last updated: 8/11/2026, 4:02:18 PM
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n,m=len(s),len(t)
        suffix=[-1]*(n+1)
        suffix[n]=m
        j=m-1
        for i in range(n-1,-1,-1):
            while j>= 0 and t[j]!=s[i]:
                j-=1
            if j==-1:
                suffix[i]=-1
            else:
                suffix[i]=j
                j-=1
        j=0
        if suffix[0]!=-1:
            return True
        for i in range(n):
            while j<m and (i==0 or t[j]!=s[i-1]):
                if i == 0:
                    break
                j+= 1
            if i>0:
                j+=1
            if i==n-1:
                return j<m
            if j<m and suffix[i+1]!=-1 and suffix[i+1]>j:
                return True
        return False
        