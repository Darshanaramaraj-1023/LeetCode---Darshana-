# Last updated: 10/5/2026, 6:37:30 AM
1class Solution:
2    def copyRandomList(self, head):
3        if not head:
4            return None
5
6        # Map original node → copied node
7        old_to_new = {}
8
9        # Step 1: Create all new nodes
10        current = head
11
12        while current:
13            old_to_new[current] = Node(current.val)
14            current = current.next
15
16        # Step 2: Connect next and random pointers
17        current = head
18
19        while current:
20            old_to_new[current].next = old_to_new.get(current.next)
21            old_to_new[current].random = old_to_new.get(current.random)
22
23            current = current.next
24
25        return old_to_new[head]