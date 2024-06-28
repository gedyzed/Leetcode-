class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        digits = [digit for digit in str(num) ]
        print(digits)

        beautyNumbers = 0
        currentdigits = ""
        digitSum = ""

        for index in range(len(digits)):
            currentdigits += digits[index] 
            
            if index >= k-1:
                currentdigits = currentdigits
                digitSum = str(currentdigits) 
                while len(digitSum) != 0 and digitSum[0] == "0":
                    digitSum = digitSum[1:]  
                    
                if len(digitSum): 
                    digitSum = int(digitSum)     
                    if num / digitSum == num // digitSum: beautyNumbers += 1 
                        
                currentdigits = currentdigits[1:]  
               

        return beautyNumbers       


        