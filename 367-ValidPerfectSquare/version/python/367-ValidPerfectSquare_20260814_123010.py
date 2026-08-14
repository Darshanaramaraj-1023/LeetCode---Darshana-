# Last updated: 8/14/2026, 12:30:10 PM
1from collections import deque
2
3class Solution:
4    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
5        result = []
6        queue = deque([root])
7
8        while queue:
9            level_sum = 0
10            level_size = len(queue)
11
12            for _ in range(level_size):
13                node = queue.popleft()
14                level_sum += node.val
15
16                if node.left:
17                    queue.append(node.left)
18
19                if node.right:
20                    queue.append(node.right)
21
22            average = level_sum / level_size
23            result.append(average)
24
25        return result