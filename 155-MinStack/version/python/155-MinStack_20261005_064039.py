# Last updated: 10/5/2026, 6:40:39 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9
10        if not self.minStack:
11            self.minStack.append(val)
12        else:
13            self.minStack.append(
14                min(val, self.minStack[-1])
15            )
16
17    def pop(self) -> None:
18        self.stack.pop()
19        self.minStack.pop()
20
21    def top(self) -> int:
22        return self.stack[-1]
23
24    def getMin(self) -> int:
25        return self.minStack[-1]