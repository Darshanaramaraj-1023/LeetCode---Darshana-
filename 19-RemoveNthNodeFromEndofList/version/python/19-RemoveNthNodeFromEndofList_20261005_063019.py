# Last updated: 10/5/2026, 6:30:19 AM
1class Solution:
2    def removeNthFromEnd(self, head, n):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        slow = dummy
7        fast = dummy
8
9        # Move fast n steps ahead
10        for _ in range(n):
11            fast = fast.next
12
13        # Move both pointers
14        while fast.next:
15            slow = slow.next
16            fast = fast.next
17
18        # Remove the node
19        slow.next = slow.next.next
20
21        return dummy.next