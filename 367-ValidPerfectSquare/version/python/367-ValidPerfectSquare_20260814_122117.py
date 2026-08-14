# Last updated: 8/14/2026, 12:21:17 PM
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        left = 0
4        right = len(letters) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if letters[mid] <= target:
10                left = mid + 1
11            else:
12                right = mid - 1
13
14        # If no greater character exists, return first character
15        return letters[left % len(letters)]