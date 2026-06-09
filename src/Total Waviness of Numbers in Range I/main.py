class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        answer = 0
        for num in range(num1, num2 + 1):
            if num < 100: continue
            stack = []
            while num > 0:
                stack.append(num % 10)
                num //= 10
            for index in range(1, len(stack) - 1):
                if stack[index] > stack[index - 1] and stack[index] > stack[index + 1]: answer += 1
                if stack[index] < stack[index - 1] and stack[index] < stack[index + 1]: answer += 1
        return answer
