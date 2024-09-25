from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes_in_arr2 = set()
        for num in arr2:
            while num > 0:
                prefixes_in_arr2.add(num)
                num //= 10
        answer = 0
        for num in arr1:
            num_str_len = len(str(num)) # Length of the total string
            while num > 0 and num and num not in prefixes_in_arr2:
                num_str_len -= 1
                num //= 10
            answer = max(num_str_len, answer)
        return answer