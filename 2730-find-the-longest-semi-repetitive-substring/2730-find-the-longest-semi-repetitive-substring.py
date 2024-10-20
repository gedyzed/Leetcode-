class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        counter = 0
        max_length = 0
        left = 0
        for right in range(len(s)) :
            
            if right > 0 and s[right - 1] == s[right]:
                counter += 1  

            while counter >= 2 and left + 1 <= right:
                if s[left] == s[left + 1]:
                    counter -= 1
                left += 1

            max_length = max(max_length,right- left + 1)
 
        return max_length           
                





        