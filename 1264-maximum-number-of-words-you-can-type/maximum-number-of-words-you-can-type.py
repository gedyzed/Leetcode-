class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        text = text.split()
        count = 0
        for i, word in enumerate(text):
            for b_letter in brokenLetters:
                if b_letter in word:
                    count += 1
                    break

        return len(text) - count            
                   

        