from typing import List

class TrieNode:
    def __init__(self, value: int = -1):
        self.children: dict[str, TrieNode] = dict()
        self.value: int = value

class FileSystem:
    def __init__(self):
        self.head = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or path == "": return False
        paths = path.split("/")
        paths.pop(0)
        current = self.head
        for i in range(len(paths) - 1):
            if paths[i] not in current.children: return False
            current = current.children[paths[i]]
        if paths[-1] in current.children: return False
        current.children[paths[-1]] = TrieNode(value)
        return True

    def get(self, path: str) -> int:
        current = self.head
        paths: List[str] = path.split("/")
        paths.pop(0)
        for p in paths:
            if p not in current.children: return -1
            current = current.children[p]
        return current.value