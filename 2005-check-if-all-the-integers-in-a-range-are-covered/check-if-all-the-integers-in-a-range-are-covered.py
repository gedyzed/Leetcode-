class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        set1 = set()
        set2 = set()

        for s, e in ranges:
            for i in range(s, e + 1):
                set1.add(i)

        for i in range(left, right + 1):
            set2.add(i) 

        return set2 <= set1            
        
     


      



