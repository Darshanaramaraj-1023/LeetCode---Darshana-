# Last updated: 10/5/2026, 6:33:27 AM
1class Solution:
2    def reorderList(self, head):
3        if not head or not head.next:
4            return
5
6        # 1. Find the middle
7        slow = head
8        fast = head
9
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14        # 2. Reverse the second half
15        second = slow.next
16        slow.next = None
17
18        prev = None
19
20        while second:
21            next_node = second.next
22            second.next = prev
23            prev = second
24            second = next_node
25
26        second = prev
27
28        # 3. Merge the two halves
29        first = head
30
31        while second:
32            first_next = first.next
33            second_next = second.next
34
35            first.next = second
36            second.next = first_next
37
38            first = first_next
39            second = second_next