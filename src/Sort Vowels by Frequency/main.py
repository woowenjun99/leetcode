class Solution:
    def sortVowels(self, s: str) -> str:
        mappers = {}
        for index, letter in enumerate(s):
            if letter not in {"a", "e", "i", "o", "u"}: continue
            if letter not in mappers: mappers[letter] = [0, index, letter]
            mappers[letter][0] -= 1
        pq = sorted(mappers.values())
        letters = list(s)
        idx = 0
        for index in range(len(letters)):
            if letters[index] not in {"a", "e", "i", "o", "u"}: continue
            letters[index] = pq[idx][2]
            pq[idx][0] += 1
            if pq[idx][0] == 0: idx += 1
        return "".join(letters)