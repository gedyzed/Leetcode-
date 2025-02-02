class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        rules = {            
            'V' : 'I',
            'X' : 'I',
            'L' : 'X',
            'C' : 'X',
            'D' : 'C',
            'M' : 'C'
        } 
        result = romans[s[0]]
        for i in range(1, len(s)):
            if s[i] in rules and s[i - 1] == rules[s[i]]:
                    result -= romans[s[i - 1]] * 2     
            result += romans[s[i]]
 
        return result          


        
        