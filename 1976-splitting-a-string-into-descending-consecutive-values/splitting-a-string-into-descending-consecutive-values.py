class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(idx):
            if idx >= len(s) :
                return len(curr) >= 2
      
            for i in range(idx, len(s)):
                num = int(s[idx: i + 1])
                if curr and curr[-1] - num != 1:
                    continue
                curr.append(num)
                if backtrack(i + 1):
                    return True 
                curr.pop()   
            return False

        curr = []
        return backtrack(0)        
        
        
        