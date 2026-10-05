# Last updated: 10/5/2026, 6:38:50 AM
1class Solution:
2    def detectCycle(self, head):
3        slow = head
4        fast = head
5
6        # Step 1: Detect whether a cycle exists
7        while fast and fast.next:
8            slow = slow.next
9            fast = fast.next.next
10
11            if slow == fast:
12                break
13        else:
14            # No cycle
15            return None
16
17        # Step 2: Find the beginning of the cycle
18        slow = head
19
20        while slow != fast:
21            slow = slow.next
22            fast = fast.next
23
24        return slow