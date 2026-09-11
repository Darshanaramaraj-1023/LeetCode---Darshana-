# Last updated: 9/11/2026, 9:03:00 AM
1class Solution:
2    def isBalanced(self, root):
3
4        def height(node):
5            if node is None:
6                return 0
7
8            left = height(node.left)
9
10            if left == -1:
11                return -1
12
13            right = height(node.right)
14
15            if right == -1:
16                return -1
17
18            if abs(left - right) > 1:
19                return -1
20
21            return max(left, right) + 1
22
23        return height(root) != -1