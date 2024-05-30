class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rankings = { letter: index for index, letter in enumerate(order) }
        letters = []
        for c in s:
            if c in rankings: letters.append((rankings[c], c))
            else: letters.append((len(s), c))
        letters.sort()
        return "".join([letter[1] for letter in letters])
