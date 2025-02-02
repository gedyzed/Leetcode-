class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for char in s:
            if char.isalnum():
                result.append(char.lower()) 

        left, right = 0, len(result) - 1  
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -=  1

        return True         





       