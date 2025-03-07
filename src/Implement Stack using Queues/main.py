from collections import deque

class MyStack:
    def __init__(self):
        self.tail = 0
        self.queues = [deque(), deque()]

    def push(self, x: int) -> None:
        self.queues[self.tail].append(x)

    def pop(self) -> int:
        while len(self.queues[self.tail]) > 1: self.queues[1 - self.tail].append(self.queues[self.tail].popleft())
        temp = self.queues[self.tail].popleft()
        self.tail = 1 - self.tail
        return temp

    def top(self) -> int:
        return self.queues[self.tail][-1]

    def empty(self) -> bool:
        return not self.queues[0] and not self.queues[1]