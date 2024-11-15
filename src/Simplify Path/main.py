class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for p in paths:
            if p == ".": continue
            if p == "..": 
                if stack: stack.pop()
                continue
            if not p: continue
            stack.append(p)
        return "/" + "/".join(stack)
