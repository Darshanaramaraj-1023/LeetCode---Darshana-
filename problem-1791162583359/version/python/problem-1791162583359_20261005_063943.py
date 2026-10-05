# Last updated: 10/5/2026, 6:39:43 AM
1class Node:
2    def __init__(self, key=0, value=0):
3        self.key = key
4        self.value = value
5        self.prev = None
6        self.next = None
7
8
9class LRUCache:
10
11    def __init__(self, capacity: int):
12        self.capacity = capacity
13        self.cache = {}
14
15        # Dummy nodes
16        self.left = Node()   # LRU side
17        self.right = Node()  # MRU side
18
19        self.left.next = self.right
20        self.right.prev = self.left
21
22    # Remove a node from the linked list
23    def remove(self, node):
24        prev_node = node.prev
25        next_node = node.next
26
27        prev_node.next = next_node
28        next_node.prev = prev_node
29
30    # Insert node just before right (MRU position)
31    def insert(self, node):
32        prev_node = self.right.prev
33
34        prev_node.next = node
35        node.prev = prev_node
36
37        node.next = self.right
38        self.right.prev = node
39
40    def get(self, key: int) -> int:
41
42        if key not in self.cache:
43            return -1
44
45        node = self.cache[key]
46
47        # This key was recently used,
48        # so move it to MRU position
49        self.remove(node)
50        self.insert(node)
51
52        return node.value
53
54    def put(self, key: int, value: int) -> None:
55
56        # If key already exists
57        if key in self.cache:
58            node = self.cache[key]
59
60            # Remove old position
61            self.remove(node)
62
63            # Update value
64            node.value = value
65
66            # Move to MRU position
67            self.insert(node)
68
69            return
70
71        # Create new node
72        node = Node(key, value)
73
74        self.cache[key] = node
75        self.insert(node)
76
77        # If capacity exceeded
78        if len(self.cache) > self.capacity:
79
80            # LRU node is just after left
81            lru = self.left.next
82
83            self.remove(lru)
84
85            del self.cache[lru.key]