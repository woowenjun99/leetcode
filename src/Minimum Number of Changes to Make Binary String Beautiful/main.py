class Solution:
    def minChanges(self, s: str) -> int:
        array = [1]
        current = s[0]
        for i in range(1, len(s)):
            if s[i] == current: array[-1] += 1
            else: 
                array.append(1)
                current = s[i]
        answer = 0
        for i in range(len(array) - 1):
            if array[i] % 2 == 0: continue
            answer += 1
            array[i + 1] -= 1
        return answer