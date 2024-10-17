class Solution:
    def maximumSwap(self, num: int) -> int:
        numeric_string = list(str(num))
        answer = num

        for i in range(len(numeric_string)):
            for j in range(i + 1, len(numeric_string)):
                numeric_string[i], numeric_string[j] = numeric_string[j], numeric_string[i]
                if int("".join(numeric_string)) > answer: answer = int("".join(numeric_string))
                numeric_string[i], numeric_string[j] = numeric_string[j], numeric_string[i]

        return answer