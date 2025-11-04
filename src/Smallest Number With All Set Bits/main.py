class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_represetation = list(bin(n))
        for i in range(len(binary_represetation) - 1, 1, -1): binary_represetation[i] = "1"
        return int("".join(binary_represetation), 2)