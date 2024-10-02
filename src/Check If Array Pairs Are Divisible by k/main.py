from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hashmap = [0] * k
        for num in arr: hashmap[num % k] += 1
        if hashmap[0] % 2 != 0: return False
        for i in range(1, len(hashmap)): 
            if hashmap[i] != hashmap[k - i]: return False
        return True
