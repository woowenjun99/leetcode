from collections import defaultdict, Counter
from itertools import combinations
from typing import List, Tuple

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        utw: List[Tuple[str, int, str]] = list(zip(username, timestamp, website))
        utw.sort()
        hashmap: defaultdict[str, List[str]] = defaultdict(list)
        for user, _, website in utw: hashmap[user].append(website)
        s = []
        for key in hashmap: s.extend(list(set(combinations(hashmap[key], 3))))
        counter = Counter(s)
        highest_score = max(counter.values())
        answer = []
        for key in counter:
            if counter[key] == highest_score:
                answer.append(key)
        answer.sort()
        return answer[0]