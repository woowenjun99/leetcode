class Solution:
    def passwordStrength(self, password: str) -> int:
        distinct_letters = set(password)
        answer = 0
        for distinct_letter in distinct_letters:
            if distinct_letter in {"!", "@", "#", "$"}: 
                answer += 5
                continue
            if ord("0") <= ord(distinct_letter) <= ord("9"):
                answer += 3
                continue
            if ord("A") <= ord(distinct_letter) <= ord("Z"):
                answer += 2
                continue
            if ord("a") <= ord(distinct_letter) <= ord("z"): answer += 1
        return answer
        