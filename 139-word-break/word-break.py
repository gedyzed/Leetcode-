class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_dicts = set(wordDict)
        memo = {}
        def dp(start):
            
            if start == len(s):
                return True
        
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dicts and dp(end):
                    memo[start] = True
                    return True
                
            memo[start] = False
            return False
        return dp(0)
                
                




            
           

            

