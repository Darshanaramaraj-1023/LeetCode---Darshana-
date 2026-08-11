# Last updated: 8/11/2026, 4:01:57 PM
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return(start[0]+start[1])%2==(target[0]+target[1])%2
        