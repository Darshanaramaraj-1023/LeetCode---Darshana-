# Last updated: 8/14/2026, 12:36:43 PM
1class Solution:
2    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
3
4        def isMirror(left, right):
5            if left is None and right is None:
6                return True
7
8            if left is None or right is None:
9                return False
10
11            if left.val != right.val:
12                return False
13
14            return isMirror(left.left, right.right) and \
15                   isMirror(left.right, right.left)
16
17        return isMirror(root.left, root.right)