# Last updated: 10/5/2026, 6:34:28 AM
1class Solution:
2    def rotateRight(self, head, k):
3        if not head or not head.next or k == 0:
4            return head
5
6        # Find length and last node
7        length = 1
8        tail = head
9
10        while tail.next:
11            tail = tail.next
12            length += 1
13
14        # Remove unnecessary full rotations
15        k = k % length
16
17        if k == 0:
18            return head
19
20        # Make the list circular
21        tail.next = head
22
23        # Find the new tail
24        steps = length - k
25        new_tail = head
26
27        for _ in range(steps - 1):
28            new_tail = new_tail.next
29
30        # New head is after new tail
31        new_head = new_tail.next
32
33        # Break the circle
34        new_tail.next = None
35
36        return new_head