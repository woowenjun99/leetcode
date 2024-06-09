from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminated = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        current = self.head
        for letter in word:
            if letter not in current.children: current.children[letter] = TrieNode()
            current = current.children[letter]
        current.terminated = True
        
    def search(self, word: str) -> bool:
        current = self.head
        stack = []
        for letter in word:
            if current.terminated: break
            if letter not in current.children: return word
            stack.append(letter)
            current = current.children[letter]
        return "".join(stack)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary: trie.insert(word)
        sentence = sentence.split()
        answer = []
        for word in sentence: answer.append(trie.search(word))
        return " ".join(answer)