class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parenthesis = []
        for index, letter in enumerate(s):
            if letter != "(" and letter != ")": continue
            if parenthesis and parenthesis[-1][0] == "(" and letter == ")": 
                parenthesis.pop()
                continue
            parenthesis.append((letter, index))
        to_delete = set(map(lambda x: x[1], parenthesis))
        new_word = []
        for i in range(len(s)):
            if i in to_delete: continue
            new_word.append(s[i])
        return "".join(new_word)