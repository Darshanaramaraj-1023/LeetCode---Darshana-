# Last updated: 8/22/2026, 9:42:52 AM
1class Solution:
2    def isValid(self, code):
3        stack = []
4        i = 0
5        n = len(code)
6
7        while i < n:
8
9            # CDATA
10            if code.startswith("<![CDATA[", i):
11                if not stack:
12                    return False
13
14                end = code.find("]]>", i + 9)
15
16                if end == -1:
17                    return False
18
19                i = end + 3
20                continue
21
22            # End tag
23            if code.startswith("</", i):
24                end = code.find(">", i + 2)
25
26                if end == -1:
27                    return False
28
29                tag = code[i + 2:end]
30
31                # Tag name must be valid
32                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
33                    return False
34
35                # Must have matching start tag
36                if not stack or stack[-1] != tag:
37                    return False
38
39                stack.pop()
40                i = end + 1
41
42                # After the outermost tag is closed,
43                # there cannot be any more content
44                if not stack and i != n:
45                    return False
46
47                continue
48
49            # Start tag
50            if code[i] == '<':
51                end = code.find('>', i + 1)
52
53                if end == -1:
54                    return False
55
56                tag = code[i + 1:end]
57
58                # Tag name must be valid
59                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
60                    return False
61
62                stack.append(tag)
63                i = end + 1
64                continue
65
66            # Normal character
67            if not stack:
68                return False
69
70            i += 1
71
72        return len(stack) == 0