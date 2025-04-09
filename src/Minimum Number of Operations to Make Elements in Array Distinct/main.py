from collections import deque
from typing import List

class Solution:
    def __is_distinct(self, counter: List[int]):
        for num in counter:
            if num == 0 or num == 1: continue
            return False
        return True

    def minimumOperations(self, nums: List[int]) -> int:
        counter = [0] * 101
        for num in nums: counter[num] += 1
        dq = deque(nums)
        answer = 0
        while not self.__is_distinct(counter) and dq:
            times_popped = 0
            while dq and times_popped < 3:
                counter[dq.popleft()] -= 1
                times_popped += 1
            answer += 1
        return answer
