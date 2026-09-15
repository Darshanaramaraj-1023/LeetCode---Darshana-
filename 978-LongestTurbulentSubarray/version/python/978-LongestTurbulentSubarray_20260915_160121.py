# Last updated: 9/15/2026, 4:01:21 PM
1from collections import deque
2
3class Solution:
4    def maxSlidingWindow(self, nums, k):
5        dq = deque()
6        result = []
7
8        for i in range(len(nums)):
9
10            # Remove elements outside the window
11            if dq and dq[0] <= i - k:
12                dq.popleft()
13
14            # Remove smaller elements
15            while dq and nums[dq[-1]] <= nums[i]:
16                dq.pop()
17
18            # Add current index
19            dq.append(i)
20
21            # Window is ready
22            if i >= k - 1:
23                result.append(nums[dq[0]])
24
25        return result