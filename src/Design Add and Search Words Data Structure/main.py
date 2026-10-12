class Node:
    def __init__(self):
        self.children = {}
        self.terminated = False

class WordDictionary:
    def __init__(self):
        self.head = Node()
        
    def addWord(self, word: str) -> None:
        current = self.head
        for c in word:
            if c not in current.children: current.children[c] = Node()
            current = current.children[c]
        current.terminated = True

    def dp(self, word: str, index: int, current: 'Node'):
        if index == len(word): return current.terminated
        if word[index] in current.children: return self.dp(word, index + 1, current.children[word[index]])
        if word[index] == ".":
            for i in range(26):
                if chr(ord("a") + i) in current.children:
                    if self.dp(word, index + 1, current.children[chr(ord("a") + i)]): return True
        return False

    def search(self, word: str) -> bool:
        return self.dp(word, 0, self.head)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)