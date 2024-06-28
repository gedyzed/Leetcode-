class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        digits = list(str(num)) 
    
        beautyNumbers = 0
        currentdigits = ""
        digitSum = ""

        for index in range(len(digits)):
            currentdigits += digits[index] 
            
            if index >= k-1:
                currentdigits = currentdigits
                digitSum = int(currentdigits) 
                if digitSum and num % digitSum == 0 : beautyNumbers += 1         
                currentdigits = currentdigits[1:]  
               

        return beautyNumbers       


        