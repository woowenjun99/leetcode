class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        index = 0
        while index < len(num_str) and num_str[index] == "9": index += 1
        a = int(num_str.replace(num_str[index], "9") if index != len(num_str) else num_str)

        b = float("inf")
        for i in range(10):
            for j in range(2):
                current = num_str.replace(str(i), str(j))
                if len(str(int(current))) < len(num_str) or str(int(current))[0] == "0": continue
                b = min(int(current), b)
        return a - b
