from typing import List

class Solution:
    def __is_palindrome_util(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left < 0 and right == len(s)

    def __is_palindrome(self, s: str):
        for i in range(len(s)):
            if self.__is_palindrome_util(s, i - 1, i + 1) or self.__is_palindrome_util(s, i, i + 1): return True
        return False

    def __backtracking(self, s: int, index: int, stack: List[int], answer: List[List[int]]):
        if index == len(s):
            for item in stack:
                if not self.__is_palindrome(item): return
            answer.append(stack.copy())
            return

        temp = stack[-1]
        stack[-1] = temp + s[index]
        self.__backtracking(s, index + 1, stack, answer)
        stack[-1] = temp
        stack.append(s[index])
        self.__backtracking(s, index + 1, stack, answer)
        stack.pop()

    def partition(self, s: str) -> List[List[str]]:
        stack = [s[0]]
        answer = []
        self.__backtracking(s, 1, stack, answer)
        return answer
