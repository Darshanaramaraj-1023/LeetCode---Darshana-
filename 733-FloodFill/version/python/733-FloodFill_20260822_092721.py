# Last updated: 8/22/2026, 9:27:21 AM
1from collections import deque
2
3class Solution:
4    def validPath(self, n, edges, source, destination):
5        # If source and destination are the same
6        if source == destination:
7            return True
8
9        # Create adjacency list
10        graph = [[] for _ in range(n)]
11
12        for u, v in edges:
13            graph[u].append(v)
14            graph[v].append(u)
15
16        # BFS
17        queue = deque([source])
18        visited = set([source])
19
20        while queue:
21            node = queue.popleft()
22
23            if node == destination:
24                return True
25
26            for neighbor in graph[node]:
27                if neighbor not in visited:
28                    visited.add(neighbor)
29                    queue.append(neighbor)
30
31        return False