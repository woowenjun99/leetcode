class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        current = n
        while current not in visited and current != 1:
            visited.add(current)
            start = 0
            while current > 0:
                start += (current % 10) ** 2
                current //= 10
            current = start
        return current == 1