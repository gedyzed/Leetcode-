class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vowels = set(["a", "i", "u", "o", "e"])
        for char in s:
            if char in vowels:
                return True

        return False        

        