class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = pow = 0
        for i in range(len(digits) - 1, -1, -1):
            num += digits[i] * (10 ** pow)
            pow += 1
        num += 1
        
        num = list(str(num))

        return  [ int(n) for n in num]  


   