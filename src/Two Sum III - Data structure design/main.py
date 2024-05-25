class TwoSum:
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        mappers = set()
        for num in self.nums:
            if num in mappers: return True
            mappers.add(value - num)
        return False