from collections import defaultdict

class Solution:
    def __dfs(self, visited: set, graph: defaultdict, letter: str, connected_component: set):
        visited.add(letter)
        connected_component.add(letter)
        for neighbour in graph[letter]:
            if neighbour in visited: continue
            self.__dfs(visited, graph, neighbour, connected_component)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mappers = defaultdict(list)
        for i in range(len(s1)):
            mappers[s1[i]].append(s2[i])
            mappers[s2[i]].append(s1[i])

        connected_components = []
        visited = set()
        for i in range(len(s1)):
            if s1[i] in visited: continue
            connected_component = set()
            self.__dfs(visited, mappers, s1[i], connected_component)
            connected_components.append(connected_component)

        for i in range(len(connected_components)): connected_components[i] = sorted(connected_components[i])
        answer = []
        for i in range(len(baseStr)):
            changed = False
            for connected_component in connected_components:
                if baseStr[i] in connected_component:
                    answer.append(connected_component[0])
                    changed = True
                    break
            if not changed: answer.append(baseStr[i])
        return "".join(answer)