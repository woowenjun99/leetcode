from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.counter: dict[int, int] = {}
        for index, num in enumerate(nums): self.counter[index] = num
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer = 0
        for i in vec.counter:
            if vec.counter[i] != 0 and self.counter[i] != 0:
                answer += vec.counter[i] * self.counter[i]
        return answer