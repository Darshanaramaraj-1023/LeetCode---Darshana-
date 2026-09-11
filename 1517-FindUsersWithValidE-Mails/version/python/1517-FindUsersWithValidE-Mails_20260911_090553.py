# Last updated: 9/11/2026, 9:05:53 AM
1class Solution:
2    def hasPathSum(self, root, targetSum):
3
4        if root is None:
5            return False
6
7        if root.left is None and root.right is None:
8            return targetSum == root.val
9
10        targetSum -= root.val
11
12        return (self.hasPathSum(root.left, targetSum) or
13                self.hasPathSum(root.right, targetSum))