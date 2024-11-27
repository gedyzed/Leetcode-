class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        left = right = 0
        s  = ""
        while left < len(word1) and right < len(word2):
            if word1[left] > word2[right]:
                s += word1[left]
                left += 1
            elif word1[left] < word2[right]:
                s += word2[right]    
                right += 1
            else:
                if word1[left : ]  > word2[right : ]:
                    s += word1[left]
                    left += 1
                else:
                    s += word2[right]  
                    right += 1
        return s + word1[left:] + word2[right:]                

                
        