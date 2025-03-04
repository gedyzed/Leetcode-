class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        # only keep one "1" to the right-end
        # keep others at the beginning

        counter = Counter(s)
        ones, zeros = counter["1"] - 1, counter["0"] 
        result = ["1" * ones] + ["0" * zeros] + ["1"]
        
        return "".join(result)


        