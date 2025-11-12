class Solution:
    def countVowels(self, word: str) -> int:

        ans = 0
        n = len(word)
        vowels = set(["a", "e", "i", "o", "u"])
        for i, chr in enumerate(word):
            if chr in vowels:
                ans += (i + 1) * (n - i)
                
        return ans



        