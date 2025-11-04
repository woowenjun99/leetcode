class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = previous_day = 1
        for i in range(n):
            if i % 7 == 0:
                total += monday
                previous_day = monday
                monday += 1
                continue
            total += 1 + previous_day
            previous_day += 1
        return total