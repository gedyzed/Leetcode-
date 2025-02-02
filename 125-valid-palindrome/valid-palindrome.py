class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for char in s:
            if char.isalnum():
                result.append(char.lower())  
        return result == result[::-1]   




       