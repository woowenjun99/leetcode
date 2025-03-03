from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        appeared = set(arr)
        answer = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                temp = [arr[i], arr[j]]
                while temp[-1] + temp[-2] in appeared: temp.append(temp[-1] + temp[-2])
                if len(temp) >= 3: answer = max(answer, len(temp))
        return answer
