# Last updated: 8/11/2026, 4:04:55 PM
class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for num in arr:
            if (num * 2) in seen:
                return True
            if num % 2 == 0 and (num // 2) in seen:
                return True
            seen.add(num)

        return False