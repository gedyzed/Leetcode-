class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        counter = Counter(s)
        ones = counter["1"] - 1
        zeros = counter["0"]
        result = ["1" * ones] + ["0" * zeros] + ["1"]
        return "".join(result)


        