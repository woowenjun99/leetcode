from collections import deque, defaultdict
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        al = defaultdict(list)
        indegrees = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] != 0: continue
                al[nums[i]].append(nums[j])
                indegrees[nums[j]] += 1

        queue = deque()
        for num in nums:
            if indegrees[num] != 0: continue
            queue.append([num, [num]])

        answer = []
        while queue:
            node, ans = queue.popleft()
            if len(ans) > len(answer): answer = ans.copy()
            for neighbour in al[node]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] != 0: continue
                queue.append([neighbour, ans.copy() + [neighbour]])
        return answer
