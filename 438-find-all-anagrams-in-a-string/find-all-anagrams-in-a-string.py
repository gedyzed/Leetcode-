class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        def check(target, window):

            for k in target.keys():
                if target[k] != window[k]:
                    return False
            return True     

        target = Counter(p)
        window = defaultdict(int)
        result, k = [], len(p)

        for right in range(len(s)):
            if s[right] in target :
                window[s[right]] += 1

            if right >= k - 1:  
                if check(target, window):    
                    result.append(right - k + 1) 
                window[s[right - k + 1]] -= 1
                               
        return result  

                 
                  