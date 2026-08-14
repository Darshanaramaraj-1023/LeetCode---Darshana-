# Last updated: 8/14/2026, 12:34:35 PM
1class Solution:
2    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
3        # Both are empty
4        if p is None and q is None:
5            return True
6
7        # One is empty, the other is not
8        if p is None or q is None:
9            return False
10
11        # Values are different
12        if p.val != q.val:
13            return False
14
15        # Compare left and right subtrees
16        return self.isSameTree(p.left, q.left) and \
17               self.isSameTree(p.right, q.right)