from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        max_heap = [(ord("a") - ord(key), -value) for key, value in counter.items()]
        heapify(max_heap)
        answer = []
        previous_letter_count = 0
        while max_heap:
            letter, count = heappop(max_heap)
            if not answer or answer[-1] != letter or previous_letter_count < repeatLimit:
                if not answer or answer[-1] != letter: previous_letter_count = 0
                answer.append(letter)
                previous_letter_count += 1
                count += 1
                if count != 0: heappush(max_heap, (letter, count))
                continue

            if not max_heap: break
            second_letter, second_count = heappop(max_heap)
            answer.append(second_letter)
            second_count += 1
            heappush(max_heap, (letter, count))
            if second_count != 0: heappush(max_heap, (second_letter, second_count))
        return "".join(list(map(lambda x: chr(ord("a") - x), answer)))
