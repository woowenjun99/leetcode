from typing import List

class Solution:
    def solve(self, graph: List[List[str]]):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        current_row = current_col = direction_index = 0
        for row in range(len(graph)):
            for col in range(len(graph[row])):
                if graph[row][col] == "^":
                    current_row = row
                    current_col = col
                    break
        visited_nodes = set()
        while True:
            if current_row + directions[direction_index][1] < 0 or current_row + directions[direction_index][1] >= len(graph) or current_col + directions[direction_index][0] < 0 or current_col + directions[direction_index][0] >= len(graph[0]):
                return len(visited_nodes) + 1
            if graph[current_row + directions[direction_index][1]][current_col + directions[direction_index][0]] == "#":
                direction_index = (direction_index + 1) % 4
                continue
            current_row += directions[direction_index][1]
            current_col += directions[direction_index][0]
            visited_nodes.add((current_row, current_col))

if __name__ == "__main__":
    with open("in.txt", "r+") as f: lines = f.readlines()
    for index in range(len(lines)): lines[index] = list(lines[index].removesuffix("\n"))
    ans = Solution().solve(lines)
    print(ans)