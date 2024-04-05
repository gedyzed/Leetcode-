class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 # points to first element
        right = len(s)-1 # points to the last element
        
        while left < right:
            s[left],s[right] = s[right],s[left] # swap elements at these two position
            left += 1
            right -= 1
            
        
        