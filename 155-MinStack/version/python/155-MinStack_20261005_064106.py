# Last updated: 10/5/2026, 6:41:06 AM
1class MinStack:
2    def __init__(self):
3        self.stack = []
4        self.minStack = []
5    def push(self, val: int) -> None:
6        self.stack.append(val)
7        if not self.minStack:
8            self.minStack.append(val)
9        else:
10            self.minStack.append(
11                min(val, self.minStack[-1])
12            )
13    def pop(self) -> None:
14        self.stack.pop()
15        self.minStack.pop()
16    def top(self) -> int:
17        return self.stack[-1]
18    def getMin(self) -> int:
19        return self.minStack[-1]