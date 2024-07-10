class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        counter = 0     
        for left in range(len(colors)):
            right = (left + 2) % len(colors)
            if colors[right-1] != colors[right]  and colors[right-1] != colors[left]:
                         counter += 1       
        return counter     
                    
                
                    
            
            
        
        
      
        