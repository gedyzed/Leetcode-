class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        def oneRow(word, row):
            for char in word:
                if char not in row:
                    return False        
            return True        

        row1, row2 = set("qwertyuiop"), set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        one_row, result = False, []

        for word in words:
            word_ = word.lower()

            if word_[0] in row1:
                one_row = oneRow(word_, row1)  
            elif word_[0] in row2:
                one_row = oneRow(word_, row2) 
            else:
                one_row = oneRow(word_, row3)

            if one_row:
                result.append(word)  
        return result        




        