from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        current = 0
        answer = []
        for num in nums:
            current ^= num
            limit = list(bin(2 ** maximumBit - 1)[2:])
            current_bin = list(bin(current)[2:])
            left = len(limit) - 1
            right = len(current_bin) - 1
            while left >= 0 and right >= 0:
                if current_bin[right] == "1": limit[left] = "0"
                else: limit[right] = "1"
                left -= 1
                right -= 1
            answer.append(int("".join(limit), 2))
        return answer[::-1]