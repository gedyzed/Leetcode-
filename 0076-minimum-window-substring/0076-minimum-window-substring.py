class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == t :
            return s

        counter = 0
        tLetters = defaultdict(int)
        for letter in t:
            tLetters[letter] += 1 

        noOfLetters =len(tLetters)
        n = len(s)
        
        sLetters = defaultdict(int)
        left , min_left = 0,0
        min_length = float('inf')

        for right in range(n):

            sLetters[s[right]] += 1
            if tLetters[s[right]] >= 1 and sLetters[s[right]] == tLetters[s[right]]:
                counter += 1

            while noOfLetters == counter :

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                sLetters[s[left]] -= 1      
                if s[left] in tLetters and  sLetters[s[left]] < tLetters[s[left]]:
                    counter -= 1      
                left += 1  

        return  s[min_left : min_left + min_length] if min_length != float('inf') else ""