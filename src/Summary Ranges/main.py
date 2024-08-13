from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answers = []
        for num in nums:
            if not answers or num > answers[-1][1] + 1:
                answers.append([num, num])
                continue
            answers[-1][1] += 1
        
        for index in range(len(answers)):
            if answers[index][0] == answers[index][1]:
                answers[index] = str(answers[index][0])
                continue
            answers[index] = str(answers[index][0]) + "->" + str(answers[index][1])
        return answers