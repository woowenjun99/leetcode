class MyHashMap:
    def __init__(self):
        self.mappers = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.mappers[key] = value

    def get(self, key: int) -> int:
        return self.mappers[key]

    def remove(self, key: int) -> None:
        self.mappers[key] = -1