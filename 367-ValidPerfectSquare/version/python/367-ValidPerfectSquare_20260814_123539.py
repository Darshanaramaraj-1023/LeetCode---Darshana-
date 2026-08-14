# Last updated: 8/14/2026, 12:35:39 PM
1class Solution:
2    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
3        if root is None:
4            return None
5
6        # Swap left and right children
7        root.left, root.right = root.right, root.left
8
9        # Invert the subtrees
10        self.invertTree(root.left)
11        self.invertTree(root.right)
12
13        return root