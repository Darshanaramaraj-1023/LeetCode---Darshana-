# Last updated: 9/15/2026, 3:49:08 PM
1class Solution:
2    def findDuplicate(self, nums):
3        # Phase 1: Find the meeting point
4        slow = nums[0]
5        fast = nums[0]
6
7        while True:
8            slow = nums[slow]
9            fast = nums[nums[fast]]
10
11            if slow == fast:
12                break
13
14        # Phase 2: Find the entrance of the cycle
15        slow = nums[0]
16
17        while slow != fast:
18            slow = nums[slow]
19            fast = nums[fast]
20
21        return slow