class MRUQueue:
    def __init__(self, n: int):
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        num = self.queue.pop(k - 1)
        self.queue.append(num)
        return num
