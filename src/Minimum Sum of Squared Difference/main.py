from collections import Counter
from sortedcontainers import SortedDict

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = []
        for i in range(len(nums1)): diff.append(abs(nums1[i] - nums2[i]))
        mappers = SortedDict(Counter(diff))
        k = k1 + k2
        while k > 0:
            key, value = mappers.popitem()
            if key == 0: return 0
            if k >= value:
                mappers[key - 1] = mappers.get(key - 1, 0) + value
                k -= value
                continue
            mappers[key] = value - k
            mappers[key - 1] = mappers.get(key - 1, 0) + k
            k = 0
        answer = 0
        for key in mappers.keys(): answer += (key ** 2) * mappers[key]
        return answer
