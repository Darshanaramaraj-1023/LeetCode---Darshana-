# Last updated: 8/22/2026, 9:18:59 AM
1class Solution:
2    def sortedArrayToBST(self, nums):
3        
4        def build(left, right):
5            if left > right:
6                return None
7            
8            mid = (left + right) // 2
9            
10            root = TreeNode(nums[mid])
11            
12            root.left = build(left, mid - 1)
13            root.right = build(mid + 1, right)
14            
15            return root
16        
17        return build(0, len(nums) - 1)