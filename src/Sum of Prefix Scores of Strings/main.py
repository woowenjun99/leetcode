from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str):
        current = self.head
        for letter in word:
            if letter not in current.children: current.children[letter] = TrieNode()
            current = current.children[letter]
            current.score += 1

    def traverse(self, word: str):
        score = 0
        current = self.head
        for letter in word:
            current = current.children[letter]
            score += current.score
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words: trie.insert(word)
        return list(map(trie.traverse, words))
