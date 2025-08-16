from typing import List

class Solution:
    def maximum69Number (self, num: int) -> int:
        stack: List[int] = []
        while num > 0:
            stack.append(num % 10)
            num //= 10
        stack = stack[::-1]
        for i in range(len(stack)):
            if stack[i] == 6:
                stack[i] = 9
                break
        answer = 0
        for i in range(len(stack)): answer = answer * 10 + stack[i]
        return answer