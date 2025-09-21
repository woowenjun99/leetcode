from collections import defaultdict
from sortedcontainers import SortedSet
from typing import List, Tuple

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented_copies = defaultdict(SortedSet)
        self.rented_copies = SortedSet()
        self.shop_movie_price: dict[Tuple[int, int], int] = {}
        for shop, movie, price in entries:
            self.unrented_copies[movie].add((price, shop))
            self.shop_movie_price[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        shops: List[int] = []
        index = 0
        while index < len(self.unrented_copies[movie]) and index < 5:
            shops.append(self.unrented_copies[movie][index][1])
            index += 1
        return shops

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.unrented_copies[movie].discard((price, shop))
        self.rented_copies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.rented_copies.discard((price, shop, movie))
        self.unrented_copies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        answer: List[Tuple[int, int]] = []
        index = 0
        while index < len(self.rented_copies) and index < 5:
            answer.append((self.rented_copies[index][1], self.rented_copies[index][2]))
            index += 1
        return answer
    