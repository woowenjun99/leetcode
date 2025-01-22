from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        updates = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            updates[start] += 1 if direction > 0 else -1
            updates[end + 1] -= 1 if direction > 0 else -1

        s = list(s)
        prefix_sum = 0
        for index in range(len(s)): 
            prefix_sum += updates[index]
            s[index] = chr((ord(s[index]) - ord("a") + prefix_sum) % 26 + ord("a"))
        return "".join(s)