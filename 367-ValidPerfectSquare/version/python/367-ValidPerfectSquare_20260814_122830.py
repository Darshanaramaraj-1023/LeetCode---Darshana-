# Last updated: 8/14/2026, 12:28:30 PM
1class Solution:
2    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
3        result = []
4
5        def postorder(node):
6            if node is None:
7                return
8
9            postorder(node.left)
10            postorder(node.right)
11            result.append(node.val)
12
13        postorder(root)
14
15        return result