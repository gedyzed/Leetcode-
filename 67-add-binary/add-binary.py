class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        
        first, second = len(a) - 1, len(b) - 1
        
        while first >= 0 or second >= 0 or carry == 1:
            if first >= 0:
                carry += int(a[first])
                first -= 1            
            if second >= 0:
                carry += int(b[second])
                second -= 1            

            res.append(str(carry % 2))
            carry = carry // 2
            
        return "".join(res[::-1])
