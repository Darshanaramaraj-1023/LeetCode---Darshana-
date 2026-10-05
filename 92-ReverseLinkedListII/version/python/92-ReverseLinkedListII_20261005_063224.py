# Last updated: 10/5/2026, 6:32:24 AM
1class Solution:
2    def reverseBetween(self, head, left, right):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        # Move prev to the node just before left
7        prev = dummy
8
9        for _ in range(left - 1):
10            prev = prev.next
11
12        # Reverse the required part
13        current = prev.next
14
15        for _ in range(right - left):
16            next_node = current.next
17
18            current.next = next_node.next
19            next_node.next = prev.next
20            prev.next = next_node
21
22        return dummy.next