from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        minutes, hours = [], []
        for i in range(60):
            set_bits = 0
            original = i
            while i > 0:
                set_bits += i % 2
                i //= 2
            minutes.append((original, set_bits))
            if original <= 11: hours.append((original, set_bits))

        answer = []
        for hour in hours:
            for minute in minutes:
                if hour[1] + minute[1] == turnedOn:
                    if minute[0] < 10: answer.append(f"{hour[0]}:0{minute[0]}")
                    else: answer.append(f"{hour[0]}:{minute[0]}")
        return answer