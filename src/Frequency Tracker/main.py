from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.counter = defaultdict(int)
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:
        if self.counter[number] > 0: self.frequencies[self.counter[number]] -= 1
        self.counter[number] += 1
        self.frequencies[self.counter[number]] += 1 

    def deleteOne(self, number: int) -> None:
        if self.counter[number] == 0: return
        self.frequencies[self.counter[number]] -= 1
        self.counter[number] -= 1
        if self.counter[number] > 0: self.frequencies[self.counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0