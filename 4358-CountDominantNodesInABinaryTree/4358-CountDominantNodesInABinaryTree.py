# Last updated: 8/11/2026, 4:02:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root):
        self.ans=0
        def dfs(node):
            if not node:
                return float('-inf')
            left_max=dfs(node.left)
            right_max=dfs(node.right)
            subtree_max = max(node.val,left_max,right_max)
            if node.val==subtree_max:
                self.ans+=1
            return subtree_max
        dfs(root)
        return self.ans
        