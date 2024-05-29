from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losers = defaultdict(int)
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            losers[match[1]] += 1
        players = sorted(players)
        answer = [[], []]
        for player in players:
            if player not in losers: answer[0].append(player)
            elif losers[player] == 1: answer[1].append(player)
        return answer