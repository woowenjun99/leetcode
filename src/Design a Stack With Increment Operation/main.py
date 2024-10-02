class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size: return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack: return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < len(self.stack) and i < k:
            self.stack[i] += val
            i += 1