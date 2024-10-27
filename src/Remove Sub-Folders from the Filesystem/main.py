from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        answer: List[str] = []
        for value in folder:
            values: List[str] = value.split("/")
            if answer:
                left = right = 0
                while left < len(answer[-1]) and right < len(values) and answer[-1][left] == values[right]:
                    left += 1
                    right += 1
                if left == len(answer[-1]): continue
            answer.append(values)
        return list(map(lambda ans: "/".join(ans), answer))