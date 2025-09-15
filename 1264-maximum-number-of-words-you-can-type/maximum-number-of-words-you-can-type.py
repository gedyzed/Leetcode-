class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        text = text.split()
        words = set()
        for bl in brokenLetters:
            for i, word in enumerate(text):
                if bl in word and (word, i) not in words:
                    words.add((word, i))

        return len(text) - len(words)            
                   

        