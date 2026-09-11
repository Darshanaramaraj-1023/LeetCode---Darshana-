# Last updated: 9/11/2026, 9:04:22 AM
1class Solution:
2    def binaryTreePaths(self, root):
3
4        result = []
5
6        def dfs(node, path):
7
8            if node is None:
9                return
10
11            path += str(node.val)
12
13            if node.left is None and node.right is None:
14                result.append(path)
15                return
16
17            path += "->"
18
19            dfs(node.left, path)
20            dfs(node.right, path)
21
22        dfs(root, "")
23
24        return result