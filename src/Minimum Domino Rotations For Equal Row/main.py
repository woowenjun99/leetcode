from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        answer = []
        count = i = 0
        while i < len(tops):
            if tops[i] != tops[0]:
                if bottoms[i] != tops[0]: break
                count += 1
            i += 1
        if i == len(tops): answer.append(count)

        count = i = 0
        while i < len(tops):
            if bottoms[i] != bottoms[0]:
                if tops[i] != bottoms[0]: break
                count += 1
            i += 1
        if i == len(tops): answer.append(count)

        count = i = 1
        while i < len(bottoms):
            if bottoms[i] != tops[0]:
                if tops[i] != tops[0]: break
                count += 1
            i += 1
        if i == len(tops): answer.append(count)

        count = i = 1
        while i < len(bottoms):
            if tops[i] != bottoms[0]:
                if bottoms[i] != bottoms[0]: break
                count += 1
            i += 1
        if i == len(tops): answer.append(count)

        return min(answer) if answer else -1
