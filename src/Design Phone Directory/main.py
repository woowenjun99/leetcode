class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.set = set(range(maxNumbers))

    def get(self) -> int:
        if len(self.set) == 0: return -1
        return self.set.pop()

    def check(self, number: int) -> bool:
        return number in self.set

    def release(self, number: int) -> None:
        self.set.add(number)