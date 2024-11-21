class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length: return -1
        current = self.head.next
        for _ in range(index): current = current.next
        return current.value

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        current = self.head
        while current is not None and current.next is not None: current = current.next
        current.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return
        previous = self.head
        current = self.head.next
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = Node(val)
        previous.next.next = current        
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length: return
        previous = self.head
        current = self.head.next
        for _ in range(index):
            previous = current
            current = current.next
        previous.next = current.next
        self.length -= 1
