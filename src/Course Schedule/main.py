from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        queue = deque([])
        count = 0

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            incoming[prerequisite[0]] += 1

        for i in range(len(incoming)):
            if not incoming[i]:
                queue.append(i)

        while queue:
            count += 1
            top = queue.popleft()
            for dest in graph[top]:
                incoming[dest] -= 1
                if not incoming[dest]: queue.append(dest)

        return count == numCourses