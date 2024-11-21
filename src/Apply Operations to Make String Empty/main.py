from collections import defaultdict, deque

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        mappers = defaultdict(deque)
        for index, value in enumerate(s): mappers[value].append(index)
        while True:
            is_last_operation = True
            for i in range(26):
                if mappers[chr(ord("a") + i)]:
                    if len(mappers[chr(ord("a") + i)]) <= 1: continue
                    is_last_operation = False
                    break

            if is_last_operation:
                arr = []
                for key in mappers:
                    if len(mappers[key]) == 0: continue
                    arr.append((mappers[key][0], key))
                arr.sort()
                return "".join(list(map(lambda x: x[1], arr)))

            for i in range(26):
                if mappers[chr(ord("a") + i)]: mappers[chr(ord("a") + i)].popleft()
