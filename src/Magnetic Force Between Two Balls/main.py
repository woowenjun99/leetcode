from typing import List

class Solution:
    def binary_search(self, position: List[int], mid: int, m: int) -> bool:
        previously_chosen = position[0]
        count = 1
        for p in range(1, len(position)):
            if position[p] - previously_chosen >= mid:
                previously_chosen = position[p]
                count += 1
        return count

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        answer = 0
        left = 1
        right = abs(position[-1] - position[0])
    
        while left <= right:
            mid = left + (right - left) // 2    # We propose that the maximum distance is mid
            count = self.binary_search(position, mid, m)
            if count >= m:
                answer = mid
                left = mid + 1
            else: right = mid - 1
        
        return answer