# Last updated: 8/22/2026, 9:30:12 AM
1from collections import defaultdict
2
3class Solution:
4    def countOfAtoms(self, formula):
5        stack = [defaultdict(int)]
6        i = 0
7        n = len(formula)
8
9        while i < n:
10            # Opening parenthesis
11            if formula[i] == '(':
12                stack.append(defaultdict(int))
13                i += 1
14
15            # Closing parenthesis
16            elif formula[i] == ')':
17                i += 1
18
19                # Read multiplier
20                num = 0
21                while i < n and formula[i].isdigit():
22                    num = num * 10 + int(formula[i])
23                    i += 1
24
25                if num == 0:
26                    num = 1
27
28                # Get the group
29                group = stack.pop()
30
31                # Multiply everything in the group
32                for atom, count in group.items():
33                    stack[-1][atom] += count * num
34
35            # Element name
36            else:
37                # First character is uppercase
38                atom = formula[i]
39                i += 1
40
41                # Read lowercase characters
42                while i < n and formula[i].islower():
43                    atom += formula[i]
44                    i += 1
45
46                # Read count
47                num = 0
48                while i < n and formula[i].isdigit():
49                    num = num * 10 + int(formula[i])
50                    i += 1
51
52                if num == 0:
53                    num = 1
54
55                stack[-1][atom] += num
56
57        # Sort atoms alphabetically
58        result = []
59
60        for atom in sorted(stack[-1]):
61            result.append(atom)
62
63            if stack[-1][atom] > 1:
64                result.append(str(stack[-1][atom]))
65
66        return ''.join(result)