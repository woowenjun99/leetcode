class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        alphabets = [chr(i + ord("a")) for i in range(26)]
        while len(word) < k:
            to_append = []
            for letter in word: to_append.append(alphabets[(ord(letter) - ord("a") + 1) % 26])
            word += "".join(to_append)
        return word[k - 1]
    