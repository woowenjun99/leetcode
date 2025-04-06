from collections import deque, defaultdict
from sortedcontainers import SortedList
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.cache = set()
        self.n = memoryLimit
        self.deque = deque()
        self.mappers = defaultdict(SortedList)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.cache: return False
        if len(self.deque) == self.n: self.forwardPacket()
        self.cache.add((source, destination, timestamp))
        self.mappers[destination].add(timestamp)
        self.deque.append((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.deque: return []
        temp = self.deque.popleft()
        self.cache.remove(temp)
        self.mappers[temp[1]].remove(temp[2])
        return list(temp)
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return self.mappers[destination].bisect_right(endTime) - self.mappers[destination].bisect_left(startTime)
