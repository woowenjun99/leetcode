from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            if not i % 15: res.append("FizzBuzz")
            elif not i % 5: res.append("Buzz")
            elif not i % 3: res.append("Fizz")
            else: res.append(str(i))

        return res