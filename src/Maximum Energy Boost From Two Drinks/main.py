from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        drinks = [energyDrinkA, energyDrinkB]
        cache = {}

        def dfs(current_hour: int, current_drink: int):
            if (current_hour, current_drink) in cache:
                return cache[(current_hour, current_drink)]

            if current_hour == n - 1:
                return drinks[current_drink][current_hour]

            change_drink = dfs(current_hour + 1, 1 - current_drink)
            dont_change_drink = dfs(current_hour + 1, current_drink) + drinks[current_drink][current_hour]
            cache[(current_hour, current_drink)] = max(change_drink, dont_change_drink)
            return cache[(current_hour, current_drink)]

        return max(dfs(0, 0), dfs(0, 1))
    
Solution().maxEnergyBoost([1,3,1], [3, 1, 1])