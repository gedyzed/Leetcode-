class Solution:
    def frequencySort(self, s: str) -> str:

        freq = defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))   
        s = ""    
        for k, v in freq.items():
            s += k * v 

        return s    


        