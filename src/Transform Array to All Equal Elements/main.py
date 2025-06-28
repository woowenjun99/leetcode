from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        ops_for_all_positive = ops_for_all_negative = 0
        cloned = nums.copy()
        cloned_two = nums.copy()
        for i in range(len(nums) - 1):
            if cloned[i] == -1:
                cloned[i] = -cloned[i]
                cloned[i + 1] = -cloned[i + 1]
                ops_for_all_positive += 1
            if cloned_two[i] == 1:
                cloned_two[i] = -cloned_two[i]
                cloned_two[i + 1] = -cloned_two[i + 1]
                ops_for_all_negative += 1
        return (ops_for_all_positive <= k and len(set(cloned)) == 1) or (ops_for_all_negative <= k and len(set(cloned_two)) == 1)