class MyQueue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        if not self.stack_two: 
            self.stack_two = self.stack_one.copy()[::-1]
            self.stack_one = []
        return self.stack_two.pop()

    def peek(self) -> int:
        if self.stack_two: return self.stack_two[-1]
        return self.stack_one[0]

    def empty(self) -> bool:
        return not self.stack_one and not self.stack_two