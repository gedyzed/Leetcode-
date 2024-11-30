class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        palindrome = ''
        for left in range(len(s)):
            sub = ""
            for right in range(left, len(s)):
                sub += s[right]   
                if sub == sub[::-1] and len(sub) > len(palindrome):
                    palindrome = sub

        return palindrome
               

        