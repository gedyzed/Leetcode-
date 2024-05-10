class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left,right = 0,0
        answer = [0]*len(s)
        temp = 0
        status = False
        notFound = False
    
        while right < len(s) and left < len(s):
  
            if s[right] == c and not status:             
                temp = right
                status = True
                
            elif right == len(s)-1 and s[right] != c:
                if not notFound:
                    left = temp+1
                    notFound = True
                answer[left] = abs(left-temp) 
                left += 1
     
            elif s[right] == c and s[temp] == c :     
                if  abs(right-left) < abs(temp-left) :                         
                    answer[left] = abs(right-left)
                else:
                    answer[left] = abs(temp-left)          
                left += 1    
                  
                if left < len(s) and left > right:
                    temp = right
                    right += 1                                     
            else:
                right += 1 
                             
        return answer     

        