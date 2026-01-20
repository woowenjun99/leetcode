from collections import deque
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Sort the events based on the time then by the message type
        events = sorted([[int(timestamp), 0 if message == "OFFLINE" else 1, string] for message, timestamp, string in events])

        answer = [0] * numberOfUsers
        offline_users = set()
        queue = deque()

        for timestamp, status, string in events:
            message = "OFFLINE" if status == 0 else "MESSAGE"
            while queue and queue[0][1] <= timestamp:
                offline_users.remove(int(queue[0][0]))
                queue.popleft()

            # Handle offline users
            if message == "OFFLINE":
                offline_users.add(int(string))
                queue.append((string, timestamp + 60))
            elif string == "ALL":
                for i in range(numberOfUsers): answer[i] += 1
                continue
            elif string == "HERE":
                for i in range(numberOfUsers):
                    if i in offline_users: continue
                    answer[i] += 1
            else:
                mentioned = string.replace("id", "").split(" ")
                for i in mentioned: answer[int(i)] += 1
        return answer