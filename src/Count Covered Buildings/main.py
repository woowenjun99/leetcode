from collections import defaultdict
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Initialise the buildings
        buildings_in_the_row = defaultdict(list)
        buildings_in_the_col = defaultdict(list)
        for row, col in buildings:
            buildings_in_the_row[row].append(col)
            buildings_in_the_col[col].append(row)

        # Sort the buildings in each row and col
        for key in buildings_in_the_row: buildings_in_the_row[key].sort()
        for key in buildings_in_the_col: buildings_in_the_col[key].sort()

        # For each building, check whether they are at the boundary either in the row or col level
        answer = 0
        for row, col in buildings:
            if buildings_in_the_row[row][0] == col or buildings_in_the_row[row][-1] == col or buildings_in_the_col[col][0] == row or buildings_in_the_col[col][-1] == row: continue
            answer += 1
        return answer