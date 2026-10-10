class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        distances = []
        current = (0, expressCost)
        for i in range(len(regular)):
            current = (
                min(current[0] + regular[i], current[1] + regular[i]), 
                min(current[0] + expressCost + express[i], current[1] + express[i])
            )
            distances.append(min(current))
        return distances