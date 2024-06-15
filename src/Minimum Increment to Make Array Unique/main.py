from typing import List
from collections import Counter, deque

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        
        # Keep track of the empty spaces
        unvisited = [True] * (10 ** 6)
        for key in keys: unvisited[key] = False
        queue = deque()
        for i in range(len(unvisited)):
            if unvisited[i]: queue.append(i)
        
        answer = 0
        for key in keys:
            while counter[key] > 1:
                while queue and queue[0] <= key: queue.popleft()
                answer += queue.popleft() - key
                counter[key] -= 1
        return answer