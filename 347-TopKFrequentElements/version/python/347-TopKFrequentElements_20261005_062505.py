# Last updated: 10/5/2026, 6:25:05 AM
1class Solution:
2    def topKFrequent(self, nums, k):
3        # Step 1: Count frequency of each number
4        freq = {}
5
6        for num in nums:
7            freq[num] = freq.get(num, 0) + 1
8
9        # Step 2: Create buckets
10        buckets = [[] for _ in range(len(nums) + 1)]
11
12        for num, count in freq.items():
13            buckets[count].append(num)
14
15        # Step 3: Take elements from highest frequency
16        result = []
17
18        for count in range(len(nums), 0, -1):
19            for num in buckets[count]:
20                result.append(num)
21
22                if len(result) == k:
23                    return result