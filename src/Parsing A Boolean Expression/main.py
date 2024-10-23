from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack: List[tuple[str, List[bool]]] = [("", [])]
        index = 0
        while index < len(expression):
            if expression[index] in {"!", "&", "|"}:
                stack.append((expression[index], []))
                index += 1 # Skip the open bracket
            elif expression[index] in {"t", "f"}: stack[-1][1].append(expression[index] == "t")
            elif expression[index] != ",":    
                exp, value = stack.pop()
                if exp == "!": stack[-1][1].append(not value[0])
                else:
                    new_value = True in value if exp == "|" else False not in value
                    stack[-1][1].append(new_value)
            index += 1
        return stack[-1][1][0]
