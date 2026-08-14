# Last updated: 8/14/2026, 12:33:33 PM
1class Solution:
2    def maxDepth(self, root: Optional[TreeNode]) -> int:
3        if root is None:
4            return 0
5
6        left_depth = self.maxDepth(root.left)
7        right_depth = self.maxDepth(root.right)
8
9        return 1 + max(left_depth, right_depth)