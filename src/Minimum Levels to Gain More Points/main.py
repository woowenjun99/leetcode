from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        for i in range(len(possible)):
            if possible[i] == 1: continue
            possible[i] = -1

        left_window_sum = possible[0]
        right_window_sum = sum(possible[1:])
        for index in range(len(possible) - 1):
            if left_window_sum > right_window_sum: return index + 1
            left_window_sum += possible[index + 1]
            right_window_sum -= possible[index + 1]
        return -1
