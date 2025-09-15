class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        text = text.split()
        words = set()

        for i, word in enumerate(text):
            # set_word = set(word)
            for b_letter in brokenLetters:
                if b_letter in word and (word, i) not in words:
                    words.add((word, i))

        return len(text) - len(words)            
                   

        