from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = deque(sentence1.split())
        sentence2 = deque(sentence2.split())
        if len(sentence1) == len(sentence2): return sentence1 == sentence2
        while sentence1 and sentence2 and sentence1[0] == sentence2[0]:
            sentence1.popleft()
            sentence2.popleft()
        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()   
        return len(sentence1) == 0 or len(sentence2) == 0
