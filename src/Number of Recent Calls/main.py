from bisect import bisect_left, bisect_right

class RecentCounter:
    def __init__(self):
        self.tracker: list[int] = []
        
    def ping(self, t: int) -> int:
        self.tracker.append(t)
        return bisect_right(self.tracker, t) - bisect_left(self.tracker, t - 3000)