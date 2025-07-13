from collections import defaultdict
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = defaultdict(int)
        count = defaultdict(int)
        for meeting in meetings:
            available_room = -1
            next_earliest_available_room = 0
            for i in range(n):
                if rooms[i] <= meeting[0]:
                    available_room = i
                    break
                if rooms[i] < rooms[next_earliest_available_room]: next_earliest_available_room = i
            
            if available_room != -1:
                rooms[available_room] = meeting[1]
                count[available_room] += 1
            else:
                rooms[next_earliest_available_room] = rooms[next_earliest_available_room] + (meeting[1] - meeting[0])
                count[next_earliest_available_room] += 1
        
        most_meetings = max(count.values())
        for i in range(n):
            if count[i] == most_meetings:
                return i