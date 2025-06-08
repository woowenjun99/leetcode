from collections import deque, defaultdict

class Solution:
    def robotWithString(self, s: str) -> str:
        mappers = defaultdict(int)
        n = len(s)
        s = deque(list(s))
        t = []
        answer = []
        for letter in s: mappers[letter] += 1

        while len(answer) < n:
            if not s:
                answer.append(t.pop())
                continue
            if not t:
                mappers[s[0]] -= 1
                t.append(s.popleft())
                continue

            exist_smaller_letter = False
            for i in range(26):
                if ord("a") + i < ord(t[-1]) and mappers[chr(ord("a") + i)]:
                    exist_smaller_letter = True
                    break
            if exist_smaller_letter: 
                mappers[s[0]] -= 1
                t.append(s.popleft())
                continue
            answer.append(t.pop())
        return "".join(answer)