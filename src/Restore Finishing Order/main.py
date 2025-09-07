from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        answer = []
        for o in order:
            if o not in friends: continue
            answer.append(o)
        return answer