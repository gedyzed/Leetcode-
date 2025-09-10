class Solution:
    def longestPalindrome(self, s: str) -> int:

        letters = Counter(s)
        length_ , odd = 0, False
        for val in letters.values():
            if val % 2 and not odd:
                length_ += val
                odd = True
            elif val % 2 and val > 1:
                length_ += val - 1
            elif val % 2 == 0:
                length_ += val

        return length_             

        