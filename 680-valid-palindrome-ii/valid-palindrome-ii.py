class Solution:
    def validPalindrome(self, s: str) -> bool:

        left_count = right_count = 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
               left_count += 1
               left += 1
            else:
                left += 1
                right -= 1

        left, right = 0, len(s) - 1        
        while left < right:
            if s[left] != s[right]:
               right_count += 1
               right -= 1
            else:
                left += 1
                right -= 1
     
        return False if left_count > 1 and right_count > 1 else True        

      



        
  
        
          
                 
