class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        combinations = [s[0]]
        answer = 0

        def recursion(index:int=1):
            nonlocal answer
            if index == len(s):
                answer = max(len(set(combinations)), answer)
                return
            temp = combinations[-1]
            combinations[-1] = temp + s[index]
            recursion(index + 1)
            combinations[-1] = temp
            combinations.append(s[index])
            recursion(index + 1)
            combinations.pop()

        recursion()
        return answer
