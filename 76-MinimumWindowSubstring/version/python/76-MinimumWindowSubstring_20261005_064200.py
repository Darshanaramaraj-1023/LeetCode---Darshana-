# Last updated: 10/5/2026, 6:42:00 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3
4        if len(t) > len(s):
5            return ""
6
7        # Count required characters
8        need = {}
9
10        for ch in t:
11            need[ch] = need.get(ch, 0) + 1
12
13        window = {}
14
15        left = 0
16        have = 0
17        need_count = len(need)
18
19        min_len = float("inf")
20        min_left = 0
21
22        for right in range(len(s)):
23
24            ch = s[right]
25            window[ch] = window.get(ch, 0) + 1
26
27            # Character requirement is satisfied
28            if ch in need and window[ch] == need[ch]:
29                have += 1
30
31            # Window contains everything required
32            while have == need_count:
33
34                # Check if current window is smaller
35                if right - left + 1 < min_len:
36                    min_len = right - left + 1
37                    min_left = left
38
39                # Remove left character
40                left_ch = s[left]
41                window[left_ch] -= 1
42
43                # Requirement is no longer satisfied
44                if left_ch in need and window[left_ch] < need[left_ch]:
45                    have -= 1
46
47                left += 1
48
49        if min_len == float("inf"):
50            return ""
51
52        return s[min_left:min_left + min_len]