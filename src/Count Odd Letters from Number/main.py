from collections import Counter

class Solution:
    def countOddLetters(self, n: int) -> int:
        mappers = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            0: "zero"
        }
        stack = []
        while n > 0:
            stack.append(mappers[n % 10])
            n //= 10
        s = "".join(stack)
        counter = Counter(s)
        return len([key for key in counter if counter[key] % 2 == 1])