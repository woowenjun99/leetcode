from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a = arr[i]
                for k in range(i + 1, j): a ^= arr[k]

                b = arr[j]
                if a == b: answer += 1
                for k in range(j + 1, len(arr)):
                    b ^= arr[k]
                    if a == b: answer += 1
        return answer