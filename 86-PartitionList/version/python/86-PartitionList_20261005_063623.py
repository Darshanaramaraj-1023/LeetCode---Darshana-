# Last updated: 10/5/2026, 6:36:23 AM
1class Solution:
2    def partition(self, head, x):
3        # Two dummy nodes
4        small_dummy = ListNode(0)
5        large_dummy = ListNode(0)
6
7        small = small_dummy
8        large = large_dummy
9
10        current = head
11
12        while current:
13            if current.val < x:
14                small.next = current
15                small = small.next
16            else:
17                large.next = current
18                large = large.next
19
20            current = current.next
21
22        # Connect the two lists
23        small.next = large_dummy.next
24
25        # Important: end the large list
26        large.next = None
27
28        return small_dummy.next