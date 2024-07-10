class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        counter = 0 
        size = len(colors)    
        for left in range(size):
            right = (left + 2) % size 
            if colors[right-1] != colors[right]  and colors[right-1] != colors[left]:
                    counter += 1               
        return counter     
                    
                
                    
            
            
        
        
      
        