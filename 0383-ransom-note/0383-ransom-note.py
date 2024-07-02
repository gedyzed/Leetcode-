class Solution:
    def canConstruct(self, ransomNote, magazine):
        alphabet = [0] * 26
        for c in ransomNote:
            idx = ord(c) - ord('a')
            i = magazine.find(c, alphabet[idx])
            if i == -1:
                return False
            alphabet[idx] = i + 1
        return True
        