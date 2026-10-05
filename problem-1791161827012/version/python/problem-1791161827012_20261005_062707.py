# Last updated: 10/5/2026, 6:27:07 AM
1import random
2
3class RandomizedSet:
4
5    def __init__(self):
6        self.nums = []
7        self.index = {}
8
9    def insert(self, val: int) -> bool:
10        if val in self.index:
11            return False
12
13        self.index[val] = len(self.nums)
14        self.nums.append(val)
15
16        return True
17
18    def remove(self, val: int) -> bool:
19        if val not in self.index:
20            return False
21
22        # Index of the element to remove
23        idx = self.index[val]
24
25        # Last element in the list
26        last = self.nums[-1]
27
28        # Move last element to the position of val
29        self.nums[idx] = last
30        self.index[last] = idx
31
32        # Remove last element
33        self.nums.pop()
34        del self.index[val]
35
36        return True
37
38    def getRandom(self) -> int:
39        return random.choice(self.nums)