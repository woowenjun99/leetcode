class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        stack = []
        answer = set()
        def backtracking():
            if len(stack) == n:
                cost = 0
                for i in range(len(stack)):
                    if stack[i] == "1":
                        cost += i
                        if i > 0 and stack[i - 1] == "1": return
                if cost <= k: answer.add("".join(stack))
                return
            stack.append("1")
            backtracking()
            stack.pop()
            stack.append("0")
            backtracking()
            stack.pop()
        backtracking()
        return list(answer)