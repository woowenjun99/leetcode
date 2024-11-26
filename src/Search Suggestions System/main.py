from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.answer = []

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str):
        current = self.head
        for letter in word:
            if letter not in current.children: current.children[letter] = TrieNode()
            current = current.children[letter]
            current.answer.append(word)
            current.answer.sort()
            if len(current.answer) > 3: current.answer.pop()

    def search(self, prefix: str) -> List[str]:
        current = self.head
        for letter in prefix:
            if letter not in current.children: return []
            current = current.children[letter]
        return current.answer

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products: trie.insert(product)
        answer = []
        prefix = ""
        for letter in searchWord:
            prefix += letter
            answer.append(trie.search((prefix)))
        return answer
