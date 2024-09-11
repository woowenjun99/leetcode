class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []
        for letter in s:
            num = ord(letter) - ord("a") + 1
            if num >= 10: nums.append(num // 10)
            nums.append(num % 10)

        for _ in range(k - 1): nums = list(map(int, list(str(sum(nums)))))
        return sum(nums)
