class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        array = [(len(word), index) for index, word in enumerate(words)]
        array.sort()
        answer = []
        for word in array: answer.append(words[word[1]].lower())
        answer[0] = answer[0].capitalize()
        return " ".join(answer)