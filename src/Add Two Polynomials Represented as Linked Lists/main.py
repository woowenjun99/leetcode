from collections import defaultdict

class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        cache = defaultdict(int)
        left = poly1
        while left:
            cache[left.power] += left.coefficient
            left = left.next
        right = poly2
        while right:
            cache[right.power] += right.coefficient
            right = right.next
        keys = sorted(cache.keys(), reverse=True)

        new_head = current = PolyNode()
        for key in keys:
            if cache[key] == 0: continue
            current.next = PolyNode(x=cache[key], y=key)
            current = current.next
        return new_head.next
