# Last updated: 8/14/2026, 12:39:19 PM
1class Solution:
2    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
3        diameter = 0
4
5        def height(node):
6            nonlocal diameter
7
8            if node is None:
9                return 0
10
11            left_height = height(node.left)
12            right_height = height(node.right)
13
14            # Diameter passing through current node
15            diameter = max(diameter, left_height + right_height)
16
17            # Return height of current node
18            return 1 + max(left_height, right_height)
19
20        height(root)
21
22        return diameter