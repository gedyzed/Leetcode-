class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        vowels = set("aeiou")
        def devowel(word):
            return "".join([char if char not in vowels else "*" for char in word ])
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vowel = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in words_cap:
                words_cap[lower] = word
            mask = devowel(lower) 
            if mask not in words_vowel:
                words_vowel[mask] = word


        ans = [""] * len(queries)
        for i, q in enumerate(queries):
            if q in words_perfect:  
                ans[i] = q
            elif q.lower() in words_cap:
                ans[i]= words_cap[q.lower()]    
            elif devowel(q.lower()) in words_vowel:
                ans[i] = words_vowel[devowel(q.lower())]    

        return ans   
             