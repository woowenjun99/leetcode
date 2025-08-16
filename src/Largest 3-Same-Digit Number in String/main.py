class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ""
        for i in range(len(num) - 2):
            if len(set([num[i], num[i + 1], num[i + 2]])) != 1: continue
            current = int(num[i] + num[i + 1] + num[i + 2])
            if answer == "" or current > int(answer): answer = num[i] + num[i + 1] + num[i + 2]
        return answer
