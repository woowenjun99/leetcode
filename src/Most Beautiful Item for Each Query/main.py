from bisect import bisect_right
from collections import defaultdict
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        price_map = defaultdict(int)
        for price, beauty in items:
            if price in price_map and price_map[price] >= beauty: continue
            price_map[price] = beauty
        answer = []
        items = sorted([(price, price_map[price]) for price in price_map])
        prices = list(map(lambda x: x[0], items))
        items = list(map(lambda x: x[1], items))
        for index in range(1, len(items)): items[index] = max(items[index], items[index - 1])
        for query in queries:
            index = bisect_right(prices, query)
            answer.append(0 if index == 0 else items[index - 1])
        return answer
