# Last updated: 8/11/2026, 4:10:40 PM
class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        i = 2
        while i * i < n:
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
            i += 1

        return sum(isPrime)