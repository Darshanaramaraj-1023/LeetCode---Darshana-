# Last updated: 8/14/2026, 12:25:17 PM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        # Sum of first k elements
4        window_sum = sum(nums[:k])
5        
6        max_sum = window_sum
7
8        # Slide the window
9        for i in range(k, len(nums)):
10            window_sum += nums[i]
11            window_sum -= nums[i - k]
12
13            max_sum = max(max_sum, window_sum)
14
15        return max_sum / k