class Solution:
    def finalString(self, s: str) -> str:
        letters = []
        for letter in s:
            if letter == "i": letters = letters[::-1]
            else: letters.append(letter)
        return "".join(letters)