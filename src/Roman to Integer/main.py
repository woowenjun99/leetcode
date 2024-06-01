class Solution:
    def romanToInt(self, s: str) -> int:
        left = answer = 0
        mappers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        while left < len(s):
            if left + 1 < len(s):
                if s[left] == "I":
                    if s[left + 1] == "V":
                        answer += 4
                        left += 2
                        continue
                    elif s[left + 1] == "X":
                        answer += 9
                        left += 2
                        continue
                if s[left] == "X":
                    if s[left + 1] == "L":
                        answer += 40
                        left += 2
                        continue
                    elif s[left + 1] == "C":
                        answer += 90
                        left += 2
                        continue
                if s[left] == "C":
                    if s[left + 1] == "D":
                        answer += 400
                        left += 2
                        continue
                    elif s[left + 1] == "M":
                        answer += 900
                        left += 2
                        continue
            answer += mappers[s[left]]
            left += 1
        return answer