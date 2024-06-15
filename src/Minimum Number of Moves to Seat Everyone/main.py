from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        answer = 0
        for seat, student in zip(seats, students): answer += abs(seat - student)
        return answer