# Last updated: 8/11/2026, 4:02:26 PM
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i=j=0
        n,m=len(series1),len(series2)
        ans=[]
        while i<n or j<m:
            if j == m or (i<n and series1[i][0]<series2[j][0]):
                t=series1[i][0]
            elif i == n or(j<m and series2[j][0]<series1[i][0]):
                t=series2[j][0]
            else:
                t=series1[i][0]
            if i<n and series1[i][0]==t:
                v1=series1[i][1]
                i+=1
            elif i<n:
                v1=series1[i][1]
            else:
                v1=0
            if j<m and series2[j][0]==t:
                v2=series2[j][1]
                j+=1
            elif j<m:
                v2=series2[j][1]
            else:
                v2=0
            ans.append([t,v1+v2])
        return ans
            