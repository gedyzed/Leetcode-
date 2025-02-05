class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        char_count = Counter(chars)
        check = count = 0
        for word in words:
            check = 0
            word_ = Counter(word)
            for key in word_:
                if word_[key] > char_count[key]:
                    break
                check += 1  

            if len(word_) == check:
                count += len(word)  
                
        return count          

            
        