from random import randint

class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        self.array.append(val)
        self.indices[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices: return False
        if len(self.array) > 1:
            last_element = self.array[-1]
            index_of_val = self.indices[val]
            self.array[-1], self.array[index_of_val] = self.array[index_of_val], self.array[-1]
            self.indices[last_element] = index_of_val
        self.array.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return self.array[randint(0, len(self.array) - 1)]