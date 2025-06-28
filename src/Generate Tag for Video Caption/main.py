class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.strip().split(" ")
        # Step 1
        for index in range(len(words)): 
            if index == 0: words[0] = words[0].lower()
            else: words[index] = words[index].capitalize()
        words = "".join(words)
        new_word = "#"
        # Step 2
        for index in range(len(words)):
            if words[index].isalpha(): new_word += words[index]
        # Step 3
        if len(new_word) > 100: new_word = new_word[:100]
        return new_word