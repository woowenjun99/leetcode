class MyHashSet:

    def __init__(self):
        self.hashset = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key]
