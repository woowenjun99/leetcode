class Solution:
    def clearDigits(self, s: str) -> str:
        while True:
            stack = []
            num_deleted = False
            for i in range(len(s)):
                if s[i] in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} and not num_deleted:
                    stack.pop()
                    num_deleted = True
                    continue
                stack.append(s[i])
            if not num_deleted: break
            s = "".join(stack)
        return s