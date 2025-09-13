class Solution:
    def maxFreqSum(self, s: str) -> int:

        max_vowel = max_cons = float('-inf')
        letters = defaultdict(int)
        for char in s:
            letters[char] += 1
            if char in ["a", "e", "i", "u", "o"]:
                max_vowel = max(max_vowel, letters[char])
            else:
                max_cons = max(max_cons, letters[char])  

        ans = 0
        if max_vowel != float('-inf'):
            ans += max_vowel
        if max_cons != float('-inf'):
            ans += max_cons
            
        return ans          
        



        