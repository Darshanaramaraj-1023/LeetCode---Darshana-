# Last updated: 8/14/2026, 12:27:09 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        result = 0
5        number = 0
6        sign = 1
7
8        for ch in s:
9            if ch.isdigit():
10                number = number * 10 + int(ch)
11
12            elif ch == '+':
13                result += sign * number
14                number = 0
15                sign = 1
16
17            elif ch == '-':
18                result += sign * number
19                number = 0
20                sign = -1
21
22            elif ch == '(':
23                # Save current result and sign
24                stack.append(result)
25                stack.append(sign)
26
27                result = 0
28                sign = 1
29
30            elif ch == ')':
31                # Complete the expression inside parentheses
32                result += sign * number
33                number = 0
34
35                # Get sign before '('
36                sign = stack.pop()
37
38                # Get result before '('
39                previous_result = stack.pop()
40
41                result = previous_result + sign * result
42
43        # Add the last number
44        result += sign * number
45
46        return result