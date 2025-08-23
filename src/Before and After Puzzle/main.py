from collections import defaultdict
from typing import List, Tuple

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        mappers: defaultdict[str, List[Tuple[str, int]]] = defaultdict(list)
        for index, phrase in enumerate(phrases):
            words = phrase.split(" ")
            mappers[words[0]].append((phrase, index))

        answer: set[str] = set()
        for i, phrase in enumerate(phrases):
            words = phrase.split(" ")
            for value in mappers[words[-1]]:
                if value[1] == i: continue
                answer.add(" ".join(words + value[0].split(" ")[1:]))
        return sorted(answer)