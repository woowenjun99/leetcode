from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = [0, 0]
        xor = 0
        for num in nums: xor ^= num
        pos_with_one = 1
        while not pos_with_one & xor: pos_with_one <<= 1
        for num in nums: answer[1 if num & pos_with_one else 0] ^= num
        return answer
