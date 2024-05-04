class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        start = 0
        end = k-1
        holder = 0
        s = list(s)
        status = False
     
        while start <= end and length :
            if k*2 <= length:
                s[start], s[end] = s[end], s[start]
                print(start,end)      
                if start == end-1 or start == end :
                    holder += k*2
                    start = holder
                    end = start + k-1
                    length = length - k*2
                    continue
                start += 1
                end -= 1 
            elif k*2 > length and length >= k:
                s[start], s[end] = s[end], s[start]
                if start == end-1:
                    break
                start += 1
                end -= 1     
            else: 
                if not status:    
                    end = end+length-k
                    status = True
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1   
      
        return "".join(s)
        