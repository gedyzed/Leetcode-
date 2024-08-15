class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:

        canA = capacityA
        canB = capacityB

        refill, left = 0, 0 
        right = len(plants) - 1
        
        while left < right:

            canA -= plants[left]
            canB -= plants[right]

            if canA < 0 :
                refill += 1
                canA = capacityA - plants[left]
            if canB < 0 :
                refill += 1
                canB = capacityB - plants[right]  
   
            left += 1
            right -= 1      
            
        if left == right: 
            canA = max(canA,canB)   
            if canA < plants[left]:
                refill += 1
            
        return refill          




                     


        
        