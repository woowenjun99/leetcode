from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.counter = [0, 0]
        self.array = [v1, v2]
        self.ptr = self.count = 0
        
    def next(self) -> int:
        if self.counter[self.ptr] >= len(self.array[self.ptr]): self.ptr = 1 - self.ptr
        num = self.array[self.ptr][self.counter[self.ptr]]
        self.counter[self.ptr] += 1
        self.ptr = 1 - self.ptr
        self.count += 1
        return num

    def hasNext(self) -> bool:
        return self.count < (len(self.array[0]) + len(self.array[1]))