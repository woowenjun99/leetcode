from heapq import heapify, heappop, heappush

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a != 0: pq.append((-a, "a"))
        if b != 0: pq.append((-b, "b"))
        if c != 0: pq.append((-c, "c"))
        heapify(pq)

        answer = ""
        while pq:
            count, letter = heappop(pq)
            if len(answer) >= 2 and answer[-1] == answer[-2] == letter:
                if not pq: return answer
                second_count, second_letter = heappop(pq)
                answer += second_letter
                second_count += 1
                if second_count != 0: heappush(pq, (second_count, second_letter))
                heappush(pq, (count, letter))
                continue
            count += 1
            answer += letter
            if count != 0: heappush(pq, (count, letter))
        return answer