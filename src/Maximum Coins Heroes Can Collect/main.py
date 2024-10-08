from bisect import bisect_right
from typing import List

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monsters_and_coins = sorted(zip(monsters, coins))
        for index, (monster, coin) in enumerate(monsters_and_coins):
            monsters[index] = monster
            coins[index] = coin

        prefix_sum = coins[0]
        for index in range(1, len(coins)):
            prefix_sum += coins[index]
            coins[index] = prefix_sum
        
        answer = []
        for hero in heroes:
            index = bisect_right(monsters, hero)
            if index == 0: answer.append(0)
            else: answer.append(coins[index - 1])
        return answer
