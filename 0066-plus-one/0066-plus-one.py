class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        answer = []
        for digit in digits:
            ans = ans * 10 + digit
        ans += 1
        
        while ans > 0 :
            num = ans % 10
            answer.insert(0,num)
            ans //= 10

        return answer          
    
            

        
        