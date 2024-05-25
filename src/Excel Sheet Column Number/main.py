class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for letter in columnTitle: result = result * 26 + ord(letter) - ord("A") + 1
        return result