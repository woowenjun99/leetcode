from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import List

class Twitter:
    def __init__(self):
        self.graph = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        if len(self.tweets[userId]) > 10: self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        queue = deque([userId] + list(self.graph[userId]))
        while queue:
            current = queue.popleft()
            for tweet in self.tweets[current]:
                heappush(pq, tweet)
                if len(pq) > 10: heappop(pq)
        pq.sort(reverse=True)
        return list(map(lambda x: x[1], pq))

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.graph: return
        self.graph[followerId].remove(followeeId)