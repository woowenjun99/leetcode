from collections import defaultdict, deque
from typing import List

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.words_with_prefix = 0

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str):
        current = self.head
        for letter in word:
            if letter not in current.children: current.children[letter] = TrieNode()
            current = current.children[letter]
            current.words_with_prefix += 1

    def search_first_prefix(self, word: str):
        current = self.head
        stack: List[str] = []
        for letter in word:
            current = current.children[letter]
            stack.append(letter)
            if current.words_with_prefix == 1: break
        if len(word) - 2 <= len(stack) <= len(word): return word
        stack.append(str(len(word) - len(stack) - 1))
        stack.append(word[-1])
        return "".join(stack)
        
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        abbreviations: defaultdict[str, deque[str]] = defaultdict(deque)
        answer: List[str] = []

        # Collate all the abbreviations together
        for word in words:
            if len(word) <= 3: continue
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
            abbreviations[abbreviation].append(word)
        
        results: defaultdict[str, deque[str]] = defaultdict(deque)
        for abbreviation in abbreviations:
            trie = Trie()
            for value in abbreviations[abbreviation]: trie.insert(value)
            for value in abbreviations[abbreviation]: results[abbreviation].append(trie.search_first_prefix(value))

        # Return the answer array
        for word in words:
            if len(word) <= 3: 
                answer.append(word)
                continue
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
            answer.append(results[abbreviation].popleft())
        return answer