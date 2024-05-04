class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        start = 0
        end = k-1
        holder = 0 #holdes the interval 
        s = list(s)
        status = False
     
        while start <= end :
            if k*2 <= length:
                s[start], s[end] = s[end], s[start]
                 
                if start == end-1 or start == end :
                    holder += k*2
                    start = holder
                    end = start + k-1
                    length = length - k*2
                    if length == 0:
                        break      
                else:
                    start += 1
                    end -= 1 
            elif k*2 > length and length >= k:
                s[start], s[end] = s[end], s[start]
                if start == end-1:
                    break
                else:
                    start += 1
                    end -= 1     
            elif k > length :
              
                if not status:    
                    end = end+length-k
                    status = True
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1   
   
        return "".join(s)
        