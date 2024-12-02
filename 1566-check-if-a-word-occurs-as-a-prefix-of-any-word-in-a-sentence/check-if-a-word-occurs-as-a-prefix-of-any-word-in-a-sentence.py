class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        n = len(searchWord)
        for i, word in  enumerate(words) : 
            if searchWord == word[: n]:
                return i + 1               
        return -1    

        