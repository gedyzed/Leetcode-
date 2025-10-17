class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_dicts = set(wordDict)
        memo = [False] * (len(s) + 1)
        memo[-1] = True
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dicts and memo[end]:
                    memo[start] = True
                    break
        
        return memo[0]








                




            
           

            

