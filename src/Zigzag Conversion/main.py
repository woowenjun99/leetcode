class Solution:
    def convert(self, s: str, numRows: int) -> str:
        stacks = [[] for _ in range(numRows)]
        stack_index = 0
        is_down = True
        for letter in s:
            stacks[stack_index].append(letter)
            if numRows == 1: continue
            stack_index = stack_index + 1 if is_down else stack_index - 1
            if stack_index == 0 or stack_index == numRows - 1: is_down = not is_down
        res = ""
        for stack in stacks: res += "".join(stack)
        return res
