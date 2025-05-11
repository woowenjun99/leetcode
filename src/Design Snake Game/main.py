from collections import deque
from typing import List

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.current = [0, 0] # ROW, COL
        self.coordinates = set()
        self.food = deque(food)
        self.queue = deque()
        self.score = 0

    def move(self, direction: str) -> int:
        directions = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1) }
        self.current[0] += directions[direction][0]
        self.current[1] += directions[direction][1]

        # Condition 1: OOB -> Game Over
        if not (0 <= self.current[0] < self.height and 0 <= self.current[1] < self.width): return -1

        # Condition 2: Encounter food
        if self.food and self.food[0] == self.current:
            self.food.popleft()
            self.coordinates.add(tuple(self.current))
            self.queue.appendleft(tuple(self.current))
            self.score += 1
            return self.score
        
        # Condition 3: Encounter tail
        self.coordinates.remove(self.queue.pop())
        if tuple(self.current) in self.coordinates: return -1

        # Condition 4: Normal movement
        self.queue.appendleft(tuple(self.current))
        self.coordinates.add(tuple(self.current))
        return self.score