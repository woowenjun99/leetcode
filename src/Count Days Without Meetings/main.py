from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        combined = []
        meetings.sort()

        for meeting in meetings:
            if not combined or combined[-1][1] < meeting[0]: combined.append(meeting)
            else: combined[-1] = [min(combined[-1][0], meeting[0]), max(combined[-1][1], meeting[1])]

        answer = days
        for combine in combined: answer -= (min(combine[1], days) - min(combine[0], days) + 1)
        return answer