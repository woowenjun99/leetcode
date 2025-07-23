from collections import defaultdict
from typing import List

class Solution:
    def __dfs(self, stack: List[str], answer: List[List[str]], mappers: List[defaultdict[str]], n: int):
        if len(stack) == n:
            for i in range(len(stack)):
                for j in range(len(stack)):
                    if stack[i][j] != stack[j][i]: return
            answer.append(stack.copy())
            return

        # Pruning Logic
        for i in range(len(stack)):
            for j in range(len(stack)):
                if stack[i][j] != stack[j][i]: return
        
        for word in mappers[stack[0][len(stack)]]:
            stack.append(word)
            self.__dfs(stack, answer, mappers, n)
            stack.pop()

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        mappers = defaultdict(list)
        for word in words: mappers[word[0]].append(word)
        answer = []
        for word in words:
            stack = [word]
            self.__dfs(stack, answer, mappers, len(words[0]))
        return answer