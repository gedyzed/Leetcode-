class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter1 = 0
        counter2 = 0
        
        
        for num in nums:     
            if num:
                counter1 += num     
            else:     
                if counter1 > counter2:  
                    counter2 = counter1
                    counter1 = 0 
                else:
                    counter1 = 0    
                    
        if counter1 > counter2:
            return counter1        
                       
        return counter2            
                       

                    
                    
        