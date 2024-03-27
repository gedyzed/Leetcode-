class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter1 = 0
        counter2 = 0
        
        swaped = False
        
        for num in nums:     
            if num == 1:
                counter1 += num
                
            else:
                if not swaped:
                    counter2 = counter1
                    counter1 = 0  
                    swaped = True
                    
                elif counter1 > counter2:  
                    counter2 = counter1
                    counter1 = 0 
                else:
                    counter1 = 0    
                    
        if counter1 > counter2:
            return counter1        
                       
        return counter2            

                    
                    
        