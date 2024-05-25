from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)

        def dfs(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if i == j or visited[j] or not isConnected[i][j]: continue
                dfs(j)

        count = 0
        for i in range(len(isConnected)):
            if visited[i]: continue
            count += 1
            dfs(i)
        return count