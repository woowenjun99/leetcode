from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        answer = 0
        what_we_have, what_we_need = set(), set()
        for i in range(len(arr)):
            what_we_need.add(i)
            what_we_have.add(arr[i])
            if what_we_have == what_we_need: answer += 1
        return answer
    