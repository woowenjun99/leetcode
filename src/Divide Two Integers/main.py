class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -pow(2, 31) and divisor == -1: return pow(2, 31) - 1
        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        d, dv = abs(dividend), abs(divisor)
        output = 0
        while d >= dv:
            temp = dv
            multiple = 1
            while d >= temp:
                d -= temp
                output += multiple
                multiple += multiple
                temp += temp
        return output if is_positive else -output