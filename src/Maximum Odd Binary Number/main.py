class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        num_of_ones = s.count("1") - 1
        new_s = ["1"] * len(s)
        for i in range(len(s) - 1):
            new_s[i] = "1" if num_of_ones > 0 else "0"
            num_of_ones -= 1
        return "".join(new_s)