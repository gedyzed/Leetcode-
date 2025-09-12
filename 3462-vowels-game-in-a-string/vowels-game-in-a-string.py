class Solution:
    def doesAliceWin(self, s: str) -> bool:

        count, vowels = 0, ["a", "i", "u", "o", "e"]
        for char in s:
            if char in vowels:
                count += 1

        return count != 0        

        