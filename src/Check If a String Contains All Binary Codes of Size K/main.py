from collections import deque

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        appeared = set()
        dq = deque()
        for i in range(k): dq.append(s[i])
        for i in range(k, len(s)):
            appeared.add("".join(dq))
            dq.popleft()
            dq.append(s[i])
        appeared.add("".join(dq))
        return len(appeared) == pow(2, k)
