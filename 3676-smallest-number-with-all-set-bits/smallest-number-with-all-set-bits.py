class Solution:
    def smallestNumber(self, n: int) -> int:
        bit_count = len(bin(n)) - 2 
        for i in range(bit_count):
            n = n | (1 << i)
        
        return n
                



        
        









        