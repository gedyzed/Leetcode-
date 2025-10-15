class Solution:
    def longestWord(self, words: List[str]) -> str:

        p_words = set([""])
        words.sort()
        ans = ""
        for word in words:
            status = False
            if word[:-1] in p_words:
                p_words.add(word)
                if len(ans) < len(word):
                    ans = word
                    status = True
        return ans
                    

            


       
        