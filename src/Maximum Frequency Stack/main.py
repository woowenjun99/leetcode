from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.counter = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        if self.max_frequency < self.counter[val]: self.max_frequency = self.counter[val]
        self.stacks[self.counter[val]].append(val)

    def pop(self) -> int:
        self.counter[self.stacks[self.max_frequency][-1]] -= 1
        temp = self.stacks[self.max_frequency].pop()
        if not self.stacks[self.max_frequency]: self.max_frequency -= 1
        return temp