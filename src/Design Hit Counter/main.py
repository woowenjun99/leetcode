from bisect import bisect_left, bisect_right

class HitCounter:
    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return bisect_right(self.timestamps, timestamp) - bisect_left(self.timestamps, timestamp - 299)