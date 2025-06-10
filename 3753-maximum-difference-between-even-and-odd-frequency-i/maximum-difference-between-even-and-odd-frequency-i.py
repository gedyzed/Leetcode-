class Solution:
    def maxDifference(self, s: str) -> int:

        counter = Counter(s)
        min_, max_ = float('inf'), float('-inf') 
        for k in counter:
            if counter[k] % 2:
                max_ = max(max_, counter[k])
            else:
                min_ = min(min_, counter[k])  

        return max_ - min_          
        