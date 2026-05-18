from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nums = defaultdict(list)
        for index, num in enumerate(arr): nums[num].append(index)
        distances = [float("inf")] * len(arr)
        distances[0] = 0
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            dist, index = queue.popleft()
            if index - 1 >= 0 and distances[index - 1] == float("inf"):
                queue.append((dist + 1, index - 1))
                distances[index - 1] = dist + 1
            if index + 1 < len(arr) and distances[index + 1] == float("inf"):
                queue.append((dist + 1, index + 1))
                distances[index + 1] = dist + 1
            if arr[index] in visited: continue # Prevent scanning the array over and over again
            for idx in nums[arr[index]]:
                if idx == index or distances[idx] != float("inf"): continue
                distances[idx] = dist + 1
                queue.append((dist + 1, idx))
            visited.add(arr[index])
        return distances[-1]
