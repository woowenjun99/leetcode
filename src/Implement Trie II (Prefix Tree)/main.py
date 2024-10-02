class TrieNode:
    def __init__(self):
        self.terminated = 0
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        current = self.head
        for letter in word:
            if letter not in current.children: current.children[letter] = TrieNode()
            current = current.children[letter]
            current.count += 1
        current.terminated += 1

    def countWordsEqualTo(self, word: str) -> int:
        current = self.head
        for letter in word:
            if letter not in current.children: return 0
            current = current.children[letter]
        return current.terminated

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.head
        for letter in prefix:
            if letter not in current.children: return 0
            current = current.children[letter]
        return current.count

    def erase(self, word: str) -> None:
        current = self.head
        for letter in word:
            if letter not in current.children: return
            current = current.children[letter]
            current.count -= 1
        current.terminated -= 1