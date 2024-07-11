from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph \
            .replace("!", " ") \
            .replace("?", " ") \
            .replace("'", " ") \
            .replace(",", " ") \
            .replace(";", " ") \
            .replace(".", " ")
        
        counter = Counter(paragraph.lower().split())
        for word in banned:
            if word in counter:
                del counter[word]
        maximum = max(counter.values())
        for word in counter:
            if counter[word] == maximum: return word