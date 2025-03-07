from bisect import bisect_right
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.items = defaultdict(list)
        self.timings = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.items[key].append(value)
        self.timings[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        right = bisect_right(self.timings[key], timestamp)
        if right == 0: return ""
        return self.items[key][right - 1]