# Last updated: 8/11/2026, 4:13:41 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return len(stack) == 0