# Last updated: 8/11/2026, 4:09:04 PM
class Solution:
    def fizzBuzz(self, n):
        answer = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer