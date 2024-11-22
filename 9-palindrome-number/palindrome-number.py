class Solution:
    def isPalindrome(self, x: int) -> bool:
     rev = 0
     n = x

     if n < 0:
        return False

     while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10 
     return rev == x