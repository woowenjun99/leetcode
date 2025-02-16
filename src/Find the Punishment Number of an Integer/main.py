from typing import List

class Solution:
    def __init__(self):
        self.is_success = False

    def __partition(self, i: int, squared: str, partitions: List[int], index: int) -> bool:
        if "".join(partitions) == squared:
            answer = sum(list(map(int, partitions)))
            if answer == i: self.is_success = True
            return

        for j in range(index, len(squared)):
            last_element = partitions[-1]
            partitions[-1] += squared[index]
            self.__partition(i, squared, partitions, j + 1)
            partitions[-1] = last_element
            self.__partition(i, squared, partitions + [str(squared[index])], j + 1)

    def punishmentNumber(self, n: int) -> int:
        answer = 0
        for i in range(1, n + 1):
            self.is_success = False
            self.__partition(i, str(i * i), [str(i * i)[0]], 1)
            if self.is_success: answer += i * i
        return answer
