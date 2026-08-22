# Last updated: 8/22/2026, 9:33:29 AM
1class NumArray:
2
3    def __init__(self, nums):
4        self.prefix = [0]
5
6        for num in nums:
7            self.prefix.append(self.prefix[-1] + num)
8
9    def sumRange(self, left, right):
10        return self.prefix[right + 1] - self.prefix[left]