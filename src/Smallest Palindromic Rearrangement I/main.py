class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = [0] * 26
        odd_count = ""
        for c in s: counter[ord(c) - ord('a')] += 1
        answer = []
        for i in range(26):
            answer += [chr(i + ord('a')) for _ in range(counter[i] // 2)]
            if counter[i] % 2 == 1: odd_count = chr(i + ord('a'))
        if odd_count != "":
            temp = answer[::-1]
            answer.append(odd_count)
            answer += temp
        else: answer += answer[::-1]
        return "".join(answer)