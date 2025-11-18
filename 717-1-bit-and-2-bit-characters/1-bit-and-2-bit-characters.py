class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits):
            if not bits[i]:
                i += 1
            else:
                if i == len(bits) - 2:
                    return False
                i += 2

        return True
            



        
        