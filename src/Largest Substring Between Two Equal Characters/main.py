from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mappers = defaultdict(list)
        for index in range(len(s)): mappers[s[index]].append(index)
        answer = -1
        for key in mappers:
            if len(mappers[key]) == 1: continue
            answer = max(answer, mappers[key][-1] - mappers[key][0] - 1)
        return answer