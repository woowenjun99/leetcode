from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        counter = Counter(hand)
        for card in hand:
            if counter[card] > 0:
                counter[card] -= 1
                for j in range(1, groupSize):
                    if counter[card + j] == 0: return False
                    counter[card + j] -= 1
        return True
