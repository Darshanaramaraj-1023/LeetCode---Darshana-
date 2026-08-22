# Last updated: 8/22/2026, 9:21:28 AM
1import heapq
2
3class Solution:
4    def lastStoneWeight(self, stones):
5        # Convert to max heap using negative values
6        stones = [-stone for stone in stones]
7        heapq.heapify(stones)
8
9        while len(stones) > 1:
10            # Get two heaviest stones
11            y = -heapq.heappop(stones)
12            x = -heapq.heappop(stones)
13
14            # If they are different, add the difference back
15            if x != y:
16                heapq.heappush(stones, -(y - x))
17
18        # Return remaining stone, or 0
19        return -stones[0] if stones else 0