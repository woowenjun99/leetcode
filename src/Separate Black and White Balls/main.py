class Solution:
    def minimumSteps(self, s: str) -> int:
        count = num_of_black = 0
        for c in s:
            if c == '0': count += num_of_black
            else: num_of_black += 1
        return count