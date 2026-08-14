# Last updated: 8/14/2026, 12:38:00 PM
1from collections import deque
2
3class Solution:
4    def minDepth(self, root: Optional[TreeNode]) -> int:
5        if root is None:
6            return 0
7
8        queue = deque([(root, 1)])
9
10        while queue:
11            node, depth = queue.popleft()
12
13            # First leaf found = minimum depth
14            if node.left is None and node.right is None:
15                return depth
16
17            if node.left:
18                queue.append((node.left, depth + 1))
19
20            if node.right:
21                queue.append((node.right, depth + 1))