class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        letters = {}
        words = {}
        count = 0
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in letters and s[i] not in words:
                letters[pattern[i]] = s[i]  
                words[s[i]] = pattern[i]  
            else:
                if letters.get(pattern[i]) != s[i] or words.get(s[i]) != pattern[i]:
                    return False   
        return True    
        