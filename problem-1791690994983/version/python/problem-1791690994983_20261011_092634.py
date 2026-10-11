# Last updated: 10/11/2026, 9:26:34 AM
1class Solution:
2    def maxPrimes(self, n: int, s: int) -> list[int]:
3        result=[]
4        total = 0
5        for num in range(2, n+1):
6            is_prime = True
7            for i in range(2, int(num ** 0.5)+1):
8                if num%i==0:
9                    is_prime=False
10                    break
11            if is_prime:
12                if total + num<=s:
13                    result.append(num)
14                    total += num
15                else:
16                    break
17        return result
18            