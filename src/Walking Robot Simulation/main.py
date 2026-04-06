from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = (0, 1)
        current = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set([tuple(obstacle) for obstacle in obstacles]) # Convert into set for O(1) lookup
        current_direction = answer = 0
        for command in commands:
            if command == -1:
                direction = directions[(current_direction + 1) % 4]
                current_direction += 1
                continue
            elif command == -2:
                direction = directions[(current_direction - 1) % 4]
                current_direction -= 1
                continue
            while command > 0:
                if (current[0] + direction[0], current[1] + direction[1]) in obstacles:
                    break
                current[0] += direction[0]
                current[1] += direction[1]
                answer = max(answer, (current[0]) ** 2 + (current[1]) ** 2)
                command -= 1
        return answer