from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player = trainer = answer = 0
        while player < len(players) and trainer < len(trainers):
            if players[player] <= trainers[trainer]:
                answer += 1
                player += 1
            trainer += 1
        return answer
