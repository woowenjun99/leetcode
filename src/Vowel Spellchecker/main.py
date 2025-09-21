from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordset: set[str] = set(wordlist)
        case_sensitivity: dict[str, str] = {}
        non_vowels: dict[str, str] = {}
        for word in wordlist:
            if word.lower() not in case_sensitivity: case_sensitivity[word.lower()] = word
            new_word: List[str] = []
            for letter in word.lower():
                if letter in {"a", "e", "i", "o", "u"}: new_word.append("_")
                else: new_word.append(letter)
            new_word = "".join(new_word)
            if new_word not in non_vowels: non_vowels[new_word] = word

        answer: List[str] = []
        for word in queries:
            if word in wordset:
                answer.append(word)
                continue
            if word.lower() in case_sensitivity:
                answer.append(case_sensitivity[word.lower()])
                continue
            new_word = []
            for letter in word.lower():
                if letter in {"a", "e", "i", "o", "u"}: new_word.append("_")
                else: new_word.append(letter)
            new_word = "".join(new_word)
            if new_word in non_vowels: 
                answer.append(non_vowels[new_word])
                continue
            answer.append("")
        return answer