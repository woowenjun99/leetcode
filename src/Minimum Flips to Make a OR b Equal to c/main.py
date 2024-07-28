class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a or b or c:
            val_a = a & 1
            val_b = b & 1
            val_c = c & 1
            if val_a == 0 and val_b == 0 and val_c == 1: answer += 1
            elif val_c == 0: 
                if val_a == 1: answer += 1
                if val_b == 1: answer += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return answer