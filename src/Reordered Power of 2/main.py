from collections import defaultdict

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power = count = 0
        cloned = n
        cloned_map: defaultdict[int, int] = defaultdict(int)
        while cloned > 0:
            cloned_map[cloned % 10] += 1
            cloned //= 10
            count += 1

        while True:
            hashmap: defaultdict[int, int] = defaultdict(int)
            x = 2 ** power
            current = 0
            while x > 0:
                hashmap[x % 10] += 1
                x //= 10
                current += 1
            if hashmap == cloned_map: return True
            elif current > count: return False
            power += 1