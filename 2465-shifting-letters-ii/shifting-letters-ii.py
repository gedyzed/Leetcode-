class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        shifted = [0] * (len(s) + 1)
        for left, right, dir in shifts:
            if dir:
                shifted[left] += 1
                shifted[right + 1] -= 1
            else:
                shifted[left] -= 1
                shifted[right + 1] += 1
   
        shift_amount = [0] * len(s)
        shift_amount[0] = shifted[0]
        for i in range(1, len(shift_amount)):
            shift_amount[i] = shifted[i] + shift_amount[i - 1]

        result = []
        for i, c in enumerate(s):
            diff = ord(c) - ord('a')
            char = chr((diff + shift_amount[i]) % 26 + 97)
            result.append(char)

        return "".join(result)    
                    
        
    

    

                
                   
                  

         
        
