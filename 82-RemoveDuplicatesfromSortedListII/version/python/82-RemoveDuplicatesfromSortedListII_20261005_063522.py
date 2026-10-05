# Last updated: 10/5/2026, 6:35:22 AM
1class Solution:
2    def deleteDuplicates(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        prev = dummy
7        current = head
8
9        while current:
10            # Check if current is part of a duplicate group
11            if current.next and current.val == current.next.val:
12
13                # Store the duplicate value
14                duplicate = current.val
15
16                # Skip all nodes with this value
17                while current and current.val == duplicate:
18                    current = current.next
19
20                # Connect previous node to the first different node
21                prev.next = current
22
23            else:
24                # Current node is unique
25                prev = current
26                current = current.next
27
28        return dummy.next