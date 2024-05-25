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
        for letter in word:
            if letter not in current.children: return False
            current = current.children[letter]
        return current.terminated

    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for letter in prefix:
            if letter not in current.children: return False
            current = current.children[letter]
        return True