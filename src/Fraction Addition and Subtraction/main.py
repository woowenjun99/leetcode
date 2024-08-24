from math import gcd

class Solution:
    def helper(self, current_numerator: int, current_denominator: int, num: int, denom: int):
        if current_numerator == 0: return num, denom
        current_numerator = num * current_denominator + current_numerator * denom
        current_denominator *= denom
        greatest_common_divisor = gcd(current_denominator, current_numerator)
        current_numerator //= greatest_common_divisor
        current_denominator //= greatest_common_divisor
        return current_numerator, current_denominator

    def fractionAddition(self, expression: str) -> str:
        current_num = ""
        current_numerator = current_denominator = 0
        for ptr in range(len(expression)):
            if expression[ptr] == "+" or (expression[ptr] == "-" and current_num != ""):
                num, denom = list(map(int, current_num.split("/")))
                if current_numerator == 0:
                    current_numerator = num
                    current_denominator = denom
                else:
                    current_numerator, current_denominator = self.helper(current_numerator, current_denominator, num, denom)
                current_num = ""
            if expression[ptr] == "+": continue
            current_num += expression[ptr]

        num, denom = list(map(int, current_num.split("/")))
        current_numerator, current_denominator = self.helper(current_numerator, current_denominator, num, denom)
        return str(current_numerator) + "/" + str(current_denominator)